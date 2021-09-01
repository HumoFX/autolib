from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from apps.university.models import University, Faculty
from api.v1.university.serializers import UniversitySerializer, FacultySerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated


class UniversityListView(ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [AllowAny]
    # pagination_class = None


class UniversityDeatilView(RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [AllowAny]


class FacultyListView(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [AllowAny]
    # pagination_class = None

# @csrf_exempt
# def faculty(request):
#     if 'GET' == request.method:
#         university = Faculty.objects.all()
#         serializer = FacultySerializer(university, many=True)
#         return JsonResponse(serializer.data, safe=False)
