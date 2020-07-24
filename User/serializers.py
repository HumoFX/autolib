from rest_framework import serializers
from .models import Users, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'last_login',
            'is_superuser',
            'username',
            'full_name',
            'university_id',
            'faculty',
            'passport_serial_id',
            'tel_num',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
        ]


