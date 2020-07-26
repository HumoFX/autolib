from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Category, UDC
from rest_framework import generics, permissions, viewsets, status
from .serializers import BookSerializer, CategorySerializer, UDCSerializer, BookSerpy, CategorySerpy
from rest_framework.permissions import AllowAny, IsAuthenticated

from .permissions import IsOwnerOrReadOnly

# Create your views here.
time4 = datetime.now()


class BookListView(generics.ListAPIView):
    # time = datetime.now()
    queryset = Book.objects.all().prefetch_related('university', 'faculty', 'udc')
    # time1 = datetime.now()
    serializer_class = BookSerializer
    # time2 = datetime.now()
    permission_classes = [IsAuthenticated]
    # time3 = datetime.now()
    # print('time1=', time1 - time, '\n time2=', time2 - time1, '\n time3=', time3 - time3, '  time=', time3 - time4)

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
    queryset = Book.objects.all().prefetch_related('university', 'faculty', 'udc')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

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
