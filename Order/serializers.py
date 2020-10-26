from rest_framework import serializers
from User.serializers import UserSerializer
from Book.serializers import BookSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # fields = ['id', 'user', 'book', 'time_of_get', 'time_of_order']
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'book', 'time_of_get', 'time_of_order', 'time_of_take_away', 'time_of_pass',
                  'active', 'done', 'retrieved']
        # fields = '__all__'


# class BookInUseSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     user = UserSerializer(read_only=True)
#     book = BookSerializer(read_only=True)
#     class Meta:
#         model = Order
#         # fields = ['id', 'user', 'book', 'time_of_get', 'time_of_order']
#         fields = ['id', 'user', 'book', 'time_of_get', 'time_of_order', 'active', 'done', 'retrieved']

# class BookInUseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookInUse
#         fields = '__all__'
