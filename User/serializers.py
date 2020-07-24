from rest_framework import serializers
from .models import Users, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


