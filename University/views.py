from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import University, Faculty
from .serializers import UniversitySerializer, FacultySerializer
from rest_framework.generics import (ListAPIView)
from rest_framework.permissions import AllowAny


# Create your views here.
#
# @csrf_exempt
# def university_list(request):
#     if request.method == 'GET':
#         university = University.objects.all()
#         serializer = UniversitySerializer(university, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UniversitySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def university_detail(request, pk):
#     try:
#         university = University.objects.get(pk=pk)
#     except University.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = UniversitySerializer(university)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = UniversitySerializer(university, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         university.delete()
#         return HttpResponse(status=204)
#

class UniversityListView(ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [AllowAny]
    # pagination_class = None


# class UniversityDeatilView(ListAPIView):
#     queryset = University.objects.all()
#     serializer_class = UniversitySerializer
#     permission_classes = [AllowAny]

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
