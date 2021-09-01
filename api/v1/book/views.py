import random

from django.core.files.storage import default_storage
from django.db.models import Value, CharField
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.book.imports import import_process
from apps.book.models import Book, Category, UDC
from api.v1.book.serializers import BookSerializer, CategorySerializer, UDCSerializer, BookDetailSerializer, \
    LabelSerializer, UserLabelSerializer

# Create your views here.
# CLIENT VIEW
from apps.label.models import Label, UserLabel
from apps.user.models import Profile
from elib.utilities.excel_export import export_from_queryset


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all().prefetch_related('university', 'udc', 'authors')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'udc__name', 'key_words']


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all().prefetch_related('university', 'udc', 'authors')
    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        queryset = Book.objects.filter(university=self.request.user.university_id.id)
        return queryset


class BookCategoryDetailView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    lookup_url_kwarg = 'category_id'

    def get_queryset(self):
        queryset = Book.objects.filter(udc_id=self.kwargs['category_id'],
                                       university=self.request.user.university_id.id).prefetch_related('university',
                                                                                                       'udc', 'authors')
        return queryset


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]


class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]


class UDCListAPIView(generics.ListAPIView):
    serializer_class = UDCSerializer
    pagination_class = None
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        qs = UDC.objects.filter(parent=None).order_by('udc')
        return qs


class UDCChildrenListAPIView(generics.ListAPIView):
    serializer_class = UDCSerializer
    permission_classes = [IsAuthenticated, ]
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        qs = UDC.objects.filter(parent=self.kwargs['id'])
        return qs


class BookUDCListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'udc_id'

    def get_queryset(self):
        queryset = Book.objects.filter(udc_new_id=self.kwargs['udc_id'],
                                       university=self.request.user.university_id.id).prefetch_related('university',
                                                                                                       'udc', 'authors')
        return queryset


@api_view(["POST"])
@csrf_exempt
def custom_upload_csv(request):
    if request.method == "POST":
        file = request.FILES["file"]
        file_name = default_storage.save(file.name, file)
        return HttpResponse(import_process(file_name))
    return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# ADMIN VIEW

class BookListAdminView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'udc__name', 'key_words']

    def get_queryset(self):
        return Book.objects.filter(university=self.request.user.university_id)


class BookDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Book.objects.all().prefetch_related('university', 'faculty', 'udc')
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        queryset = Book.objects.filter(university=self.request.user.university_id.id)
        return queryset


class CategoryListAdminView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]


class CategoryDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]


class BookLabelingExportView(APIView):
    """ Возвращает список тех книг, у которых нет tag_id для объекта Label"""
    def post(self, request, *args, **kwargs):
        """POST запрос с пустым телом вернет список с ключом data, в котором будут сколько объектов Label было
        создано для книги с новыми инвентарными номерами. [Временный метод]"""
        user = request.user
        books = Book.objects.filter(university=user.university_id)
        data = []
        for book in books:
            # print(book.inventory_list)
            new_label = []
            # if not Label.objects.filter(book_id=book.id).exists():
            for inventory in book.inventory_list:
                if not Label.objects.filter(inventory=str(inventory), book_id=book.id).exists():
                    rand_pass = str(random.randint(0, 99999999))
                    rand_pass.zfill(8)
                    new_label.append(
                        Label(book=book, inventory=inventory, password=rand_pass, university=user.university_id))
            labels = Label.objects.bulk_create(new_label)
            if labels:
                data.append({"book": book.id, "count": len(labels)})
        # print(data)
        return Response(data={"data": data}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        """Возвращает список Label у которых нет tag_id(то есть метка не зарегистрирована для книги)"""
        user = request.user
        labels = Label.objects.filter(university=user.university_id, tag_id__isnull=True)
        # fields = ['book.title', 'inventory', 'book_id', 'type', 'password', 'id']
        # file = export_from_queryset(queryset=labels, fields=fields)
        # content_type = 'application/vnd.ms-excel'
        # response = HttpResponse(file, content_type=content_type)
        # Book.objects.filter()
        # return response
        serializer = LabelSerializer(labels, many=True)
        return Response(serializer.data)


class UserLabelingExportView(APIView):
    # def post(self, request, *args, **kwargs):
    #     user = request.user
    #     profiles = Profile.objects.filter(university=user.university_id)
    #     data = []
    #     for profile in profiles:
    #         # print(book.inventory_list)
    #         new_label = []
    #         # if not Label.objects.filter(book_id=book.id).exists():
    #         for inventory in book.inventory_list:
    #             if not Label.objects.filter(inventory=str(inventory), book_id=book.id).exists():
    #                 rand_pass = str(random.randint(0, 99999999))
    #                 rand_pass.zfill(8)
    #                 new_label.append(
    #                     Label(book=book, inventory=inventory, password=rand_pass, university=user.university_id))
    #         labels = Label.objects.bulk_create(new_label)
    #         if labels:
    #             data.append({"book": book.id, "count": len(labels)})
    #     # print(data)
    #     return Response(data={"data": data}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        """ Возвращает excel с UserLabel, у которых не зарегистрированы метки"""
        user = request.user
        labels = UserLabel.objects.filter(university=user.university_id, tag_id__isnull=True).annotate(
            type=Value('user', output_field=CharField()))
        fields = ['user.full_name', 'inventory', 'user_id', 'type', 'id']
        file = export_from_queryset(queryset=labels, fields=fields)
        content_type = 'application/vnd.ms-excel'
        response = HttpResponse(file, content_type=content_type)
        Book.objects.filter()
        return response


class UserLabelListView(generics.ListAPIView):
    """ Возвращает список с UserLabel, у которых не зарегистрированы метки"""
    serializer_class = UserLabelSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = UserLabel.objects.filter(university=user.university_id, tag_id__isnull=True)
        return queryset


class LabelsUpdateApiView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            for data in request.data['labels']:
                label = get_object_or_404(Label, pk=data['id'])
                if label:
                    label.tag_id = data['tag_id']
                    label.save()
            return Response({'ok': True}, status=status.HTTP_200_OK)
        except:
            return Response({"ok": False}, status=status.HTTP_400_BAD_REQUEST)


class UserLabelsUpdateApiView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            for data in request.data['labels']:
                label = get_object_or_404(UserLabel, pk=data['id'])
                if label:
                    label.tag_id = data['tag_id']
                    label.save()
            return Response({'ok': True}, status=status.HTTP_200_OK)
        except:
            return Response({"ok": False}, status=status.HTTP_400_BAD_REQUEST)


class LabelIdentifyAPIView(RetrieveAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.filter(tag_id__isnull=False)
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'id'

    def get_object(self):
        university = self.request.user.university_id
        obj = Label.objects.filter(inventory=self.kwargs.get('id'), university=university).last()
        return obj


class UserLabelIdentifyAPIView(RetrieveAPIView):
    serializer_class = UserLabelSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'id'

    def get_object(self):
        university = self.request.user.university_id
        obj = UserLabel.objects.filter(inventory=self.kwargs.get('id'), university=university).last()
        return obj
