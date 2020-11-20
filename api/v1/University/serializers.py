from rest_framework import serializers
from .models import University, Faculty


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

    def to_representation(self, instance):
        response = super(UniversitySerializer, self).to_representation(instance)
        if instance.logo:
            response['logo'] = instance.logo.url
        return response


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

