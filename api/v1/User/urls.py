from django.conf.urls import url
from django.urls import path, include

from .views import UserCreateView,UserDetailView, RefreshTokenView, ObtainTokenPairView
from .forms import MyCustomUserForm

urlpatterns = [
    path('user/', UserCreateView.as_view(), name='create profile'),
    path('user/<int:pk>', UserDetailView.as_view(), name='crud profile'),
]
