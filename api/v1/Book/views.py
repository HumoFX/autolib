from datetime import datetime

from django.core.signals import request_started, request_finished
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
import time
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Category, UDC
from rest_framework import generics, permissions, viewsets, status
from .serializers import BookSerializer, CategorySerializer, UDCSerializer, BookSerpy, CategorySerpy
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import filters

from .permissions import IsOwnerOrReadOnly


# Create your views here.
# CLIENT VIEW

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all().prefetch_related('university', 'udc')
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'udc__name', 'key_words']

    # def get_queryset(self):
    #     queryset = Book.objects.filter(university=self.request.user.university_id.id).prefetch_related('university'
    #                                                                                                 ,'faculty')
    #     return queryset
    # serializer_time = time.time() - serializer_start
    # if request_started:
    #     db_start = datetime.now()
    #     db_time = datetime.now() - db_start
    #
    #     serializer_start = datetime.now()
    #     # time1 = datetime.now()
    #     serializer_class = BookSerializer
    #     serializer_time = datetime.now() - serializer_start
    #     # time2 = datetime.now()
    #     permission_classes = [AllowAny]
    #     # time3 = datetime.now() print('time1=', time1 - time, '\n time2=', time2 - time1, '\n time3=',
    #     # time3 - time3, '  time=', time3 - time4)
    #     print('db_time', db_time, '\nserializer_time=', serializer_time)
    #
    # if request_finished:
    #     end_time = datetime.now() - db_start
    #     print('end_time=', end_time)
    # def list(self, request):
    #     global serializer_time
    #     global db_time
    #
    #     db_start = time.time()
    #     books = Book.objects.all()
    #     # print(books)
    #     db_time = time.time() - db_start
    #     serializer_start = time.time()
    #     serializer = BookSerializer(books, many=True)
    #     # print(serializer)
    #     serializer_time = time.time() - serializer_start
    #
    #     return Response(serializer.data)

    # def dispatch(self, request, *args, **kwargs):
    #     global dispatch_time
    #     global render_time
    #
    #     dispatch_start = time.time()
    #     ret = super(BookListView, self).dispatch(request, *args, **kwargs)
    #     render_start = time.time()
    #     ret.render()
    #     render_time = time.time() - render_start
    #
    #     dispatch_time = time.time() - dispatch_start
    #
    #     return ret
    #
    # def started(sender, **kwargs):
    #     global started
    #     started = time.time()
    #
    # def finished(sender, **kwargs):
    #     total = time.time() - started
    #     api_view_time = dispatch_time - (render_time + serializer_time + db_time)
    #     request_response_time = total - dispatch_time
    #
    #     print("Database lookup               | %.4fs" % db_time)
    #     print("Serialization                 | %.4fs" % serializer_time)
    #     print("Django request/response       | %.4fs" % request_response_time)
    #     print("API view                      | %.4fs" % api_view_time)
    #     print("Response rendering            | %.4fs" % render_time)
    #
    # request_started.connect(started)
    # request_finished.connect(finished)


#
# time5 = datetime.now()
# print('\ntime4-5', time5 - time4)


# def list(self, request):
#     try:
#         data = Book.objects.all()
#     except Exception as e:
#         return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
#     return Response(BookSerpy(data, many=True).data, status=status.HTTP_200_OK)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Book.objects.all().prefetch_related('university', 'faculty', 'udc')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        queryset = Book.objects.filter(university=self.request.user.university_id.id)
        return queryset


class BookCategoryDetailView(generics.ListAPIView):
    # queryset = Book.objects.all().prefetch_related('university', 'faculty', 'udc')
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    lookup_url_kwarg = ['category_id']

    def get_queryset(self):
        queryset = Book.objects.filter(udc_id=self.kwargs['category_id'])
        return queryset


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]


# ADMIN VIEW

class BookListAdminView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'udc__name', 'key_words']


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


@csrf_exempt
@api_view(('GET',))
@renderer_classes(JSONRenderer)
def book_list(request):
    time_start = datetime.now()
    if request.method == 'GET':
        time_1 = datetime.now()
        books = Book.objects.all()
        time_2 = datetime.now()
        serializer = BookSerpy(books, many=True)
        time_3 = datetime.now()
        print('time start', time_1 - time_start, '\n time1=', time_2 - time_1, '\n time2=', time_3 - time_2,
              '\n time3=', time_3 - time_start)
        return Response(serializer.data)
    else:
        return HttpResponse(status=401)
        # time_new = datetime.now()
        # print('neeew',time_new-time3)


@csrf_exempt
@api_view(('GET',))
@renderer_classes(JSONRenderer)
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET' and request.user.has_perm(perm=IsAuthenticated):
        serializer = BookSerpy(book)
        return Response(serializer.data)
    return HttpResponse(status=401)


@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerpy(category, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerpy(category)
        return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = CategorySerializer(category, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         category.delete()
#         return HttpResponse(status=204)
#
#
