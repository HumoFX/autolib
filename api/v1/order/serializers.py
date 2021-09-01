from notifications.signals import notify
from rest_framework import serializers
from api.v1.user.serializers import UserSerializer
from api.v1.book.serializers import BookSerializer
from apps.order.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        # fields = ['id', 'user', 'book', 'time_of_get', 'time_of_order']
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['status'] = instance.status
        return response


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

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
        fields = ('id', 'user', 'book', 'time_of_get', 'time_of_order', 'time_of_take_away', 'time_of_pass',
                  'active', 'done', 'retrieved')
        # fields = '__all__'

    def update(self, instance, validated_data):
        active = validated_data['active']
        done = validated_data['done']
        retrieved = validated_data['retrieved']
        user = instance.user
        print(user)
        if instance.active and not active:
            if done:
                notify.send(user, recipient=user, verb='you took a book')
            else:
                notify.send(user, recipient=user, verb='your order where deactivated')
        elif not instance.active and instance.done:
            if not instance.retrieved and retrieved:
                notify.send(user, recipient=user, verb='you received a book to library')

        instance.active = active
        instance.done = done
        instance.retrieved = retrieved
        instance.time_of_pass = validated_data.get('time_of_pass', instance.time_of_pass)
        instance.time_of_take_away = validated_data.get('time_of_take_away', instance.time_of_take_away)
        instance.save()
        return instance
