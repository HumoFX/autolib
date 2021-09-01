from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Profile
from api.v1.user.serializers import UserSerializer, RefreshTokenSerializer, ObtainTokenPairSerializer
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, )
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from api.v1.user.permissions import IsOwnerOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'librarian/index.html'
