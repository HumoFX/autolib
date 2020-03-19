from rest_framework import serializers
from .models import Order, BookInUse


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class BookInUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInUse
        fields = '__all__'

