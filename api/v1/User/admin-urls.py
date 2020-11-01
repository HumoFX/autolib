from django.conf.urls import url
from django.urls import path, include
from django_registration.views import RegistrationView

from .views import UserListAdminView,UserDetailView, RefreshTokenView, ObtainTokenPairView
from .forms import MyCustomUserForm

urlpatterns = [
    path('user/', UserListAdminView.as_view(), name='list profiles'),
    path('user/<int:pk>', UserDetailView.as_view(), name='read only profile'),

]
