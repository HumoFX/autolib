from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import University
from .serializers import UniversitySerializer


# Create your views here.

@csrf_exempt
def university_list(request):
    if request.method == 'GET':
        university = University.objects.all()
        serializer = UniversitySerializer(university, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UniversitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def university_detail(request, pk):
    try:
        university = University.objects.get(pk=pk)
    except University.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UniversitySerializer(university)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UniversitySerializer(university, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        university.delete()
        return HttpResponse(status=204)

