from abc import ABC
from datetime import datetime
from functools import partial

from rest_framework import serializers

from University.models import Faculty
from .models import Book, Category, UDC
from User.models import Profile
from typing import Dict, Any
import serpy
from User.serializers import UserSerializer
from University.serializers import UniversitySerializer, FacultySerializer


class BookSerpy(serpy.Serializer):
    # time = datetime.now()
    id = serpy.MethodField()
    title = serpy.StrField()
    author = serpy.StrField()
    udc = serpy.MethodField()
    isbn = serpy.StrField()
    key_words = serpy.StrField()
    university = serpy.MethodField()
    faculty = serpy.MethodField()
    quantity = serpy.IntField()
    price = serpy.FloatField()
    rating = serpy.FloatField()
    used = serpy.IntField()
    img = serpy.StrField()
    e_book = serpy.BoolField()
    file = serpy.StrField()
    printed_book = serpy.BoolField()
    special_books = serpy.BoolField()
    work_book = serpy.BoolField()
    date_pub = serpy.Field()
    date_get = serpy.Field()
    created = serpy.Field()

    def get_id(self, obj):
        if obj is not None:
            return obj.pk

    def get_udc(self, obj):
        if obj is not None:
            return obj.udc.pk

    def get_university(self, obj):
        # a = Profile.objects.get(pk=obj.university)
        # print(a)
        # print(obj.university.pk)
        if obj is not None:
            return obj.university.pk

    def get_faculty(self, obj):
        if obj is not None:
            return obj.faculty.pk

    # time1 = datetime.now()
    # print('\n serpy=', time1 - time)


class CategorySerpy(serpy.Serializer):
    id = serpy.MethodField()
    udc_id = serpy.StrField()
    name = serpy.StrField()
    parent = serpy.MethodField()

    def get_id(self, obj):
        if obj is not None:
            return obj.pk

    def get_parent(self, obj):
        if obj is not None:
            return obj.parent


# class UDCSerpy(serpy.Serializer):
#     id = serpy.MethodField()
#     id_number = serpy.StrField()

#     def as_getter(self, serializer_field_name, serializer_cls):
#         return partial(get_related, serializer_field_name)
#
#
# def get_related(name, instance):
#     value = getattr(instance, name, None)
#     if value and is_related(instance._meta, value):
#         value = value.all()
#     return value
#
#
# def is_related(opts, value):
#     field = None
#     if hasattr(value, 'field'):
#         field = value.field
#     if not field and hasattr(value, 'source_field'):
#         field = value.source_field
#     if field and hasattr(field, 'remote_field'):
#         return (
#                 field.remote_field in related_fields(opts) or value.field in many_to_many_fields(opts)
#         )
#     return False
#
#
# def related_fields(opts):
#     return (
#         f for f in opts.get_fields(include_hidden=True)
#         if f.auto_created and not f.concrete and (f.one_to_one or f.one_to_many)
#     )
#
#
# def many_to_many_fields(opts):
#     return (
#         f for f in opts.get_fields(include_hidden=True)
#         if f.many_to_many and f.auto_created
#     )


# def serialize_user(obj: Book) -> Dict[str, Any]:
#     return {
#         "id": obj.id,
#         "title": obj.title,
#         "author": obj.author,
#         "isbn": obj.isbn,
#         "key_words": obj.key_words,
#         "img": obj.img,
#         "quantity": obj.quantity,
#         "price": obj.price,
#         "rating": obj.rating,
#         "used": obj.used,
#         "e_book": obj.e_book,
#         "file": obj.file,
#         "printed_book": obj.printed_book,
#         "special_books": obj.special_books,
#         "work_book": obj.work_book,
#         "date_pub": obj.date_pub,
#         "date_get": obj.date_get,
#         "created": obj.created,
#         "udc": obj.udc,
#         "university": obj.university,
#         "faculty": obj.faculty
#     }

class UDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = UDC
        # fields = ('id', 'id_number')

    fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # udc_id = UDCSerializer

    class Meta:
        model = Category
        # fields = ('id', 'udc_id', 'name', 'parent')
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # time = datetime.now()
    #
    # udc = UDCSerializer
    # university = UserSerializer
    # faculty = FacultySerializer

    # id = serializers.IntegerField()
    # title = serializers.CharField()
    # author = serializers.CharField()
    # udc = serializers.PrimaryKeyRelatedField(read_only=True)
    # isbn = serializers.CharField()
    # key_words = serializers.CharField()
    # university = serializers.PrimaryKeyRelatedField(read_only=True)
    # faculty = serializers.PrimaryKeyRelatedField(read_only=True)
    # quantity = serializers.IntegerField()
    # price = serializers.FloatField()
    # rating = serializers.FloatField()
    # used = serializers.IntegerField()
    # img = serializers.ImageField()
    # e_book = serializers.BooleanField()
    # file = serializers.FileField()
    # printed_book = serializers.BooleanField()
    # special_books = serializers.BooleanField()
    # work_book = serializers.BooleanField()
    # date_pub = serializers.DateField()
    # date_get = serializers.DateField()
    # created = serializers.DateField()
    class Meta:
        model = Book
        # fields = ('id', 'title', 'author', 'udc', 'isbn', 'key_words', 'img',
        #           'faculty', 'quantity', 'price', 'rating',
        #           'used', 'e_book', 'file', 'printed_book', 'special_books',
        #           'work_book', 'date_pub', 'date_get', 'created')
        fields = '__all__'
        # read_only_fields = ('id', 'title', 'author', 'udc', 'isbn', 'key_words', 'img',
        #                     'university', 'faculty', 'quantity', 'price', 'rating',
        #                     'used', 'e_book', 'file', 'printed_book', 'special_books',
        #                     'work_book', 'date_pub', 'date_get', 'created')

    # time1 = datetime.now()
    # print('\n ModelSerializer', time1 - time)
