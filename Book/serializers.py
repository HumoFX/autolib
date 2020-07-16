from rest_framework import serializers
from .models import Book, Category, UDC


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = UDC
        fields = '__all__'
