from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Profile
from .serializers import UserSerializer, RefreshTokenSerializer, ObtainTokenPairSerializer
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, )
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .permissions import IsOwnerOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer


# Create your views here.
class UserCreateView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    # pagination_class = None

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(user=user)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
    # pagination_class = None


class UserListAdminView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
#
# @csrf_exempt
# def user_list(request):
#     if request.method == 'GET':
#         user = Users.objects.all()
#         serializer = UserSerializer(user, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def user_detail(request, pk):
#     try:
#         user = Users.objects.get(pk=pk)
#     except Users.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=204)

class RefreshTokenView(TokenRefreshView):
    serializer_class = RefreshTokenSerializer


class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = ObtainTokenPairSerializer
