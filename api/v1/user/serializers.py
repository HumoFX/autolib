from rest_framework import serializers
from apps.user.models import Profile
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
            'is_active',
        ]

    def to_representation(self, instance: Profile):
        response = super(UserSerializer, self).to_representation(instance)
        response['university_name'] = instance.university_id.name
        response['faculty_name'] = instance.faculty.name
        if instance.avatar:
            response['avatar'] = self.context['request'].build_absolute_uri(instance.avatar.url)
        return response


class UserShortSerializer(serializers.ModelSerializer):
    faculty = serializers.CharField(source='faculty.name')

    class Meta:
        model = Profile
        fields = ['id', 'full_name', 'faculty', 'group_name', 'tel_num', 'kafedra']
