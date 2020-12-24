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
from .serializers import BookSerializer, CategorySerializer, UDCSerializer, BookSerpy, BookDetailSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsOwnerOrReadOnly


# Create your views here.
# CLIENT VIEW

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
    pagination_class = None
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
