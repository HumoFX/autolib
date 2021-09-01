from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path, include

from .views import UserCreateView, UserDetailView, RefreshTokenView, ObtainTokenPairView, IndexView

app_name = 'user'
urlpatterns = [
    path('user/', UserCreateView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('me/', UserDetailView.as_view()),
]
