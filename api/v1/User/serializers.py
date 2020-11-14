from rest_framework import serializers
from .models import Profile
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenObtainPairSerializer
from rest_framework.validators import ValidationError


class RefreshTokenSerializer(TokenRefreshSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        if user.is_staff:
            return token
        else:
            raise ValidationError("Idi naxooy")


class ObtainTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(user.is_staff)
        if user.is_staff:
            return token
        else:
            raise ValidationError("Idi naxooy")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'is_superuser',
            'username',
            'full_name',
            'university_id',
            'faculty',
            'group_name',
            'avatar',
            'kafedra',
            'position',
            'passport_serial_id',
            'tel_num',
            'email',
            'is_staff',
            'is_active',
        ]

    def to_representation(self, instance):
        response = super(UserSerializer, self).to_representation(instance)
        if instance.avatar:
            response['avatar'] = instance.avatar.url
        return response
        # fields = '__all__'
