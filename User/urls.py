from django.conf.urls import url
from django.urls import path, include
from django_registration.views import RegistrationView

from .views import UserCreateListView,UserDetailView
from User.forms import MyCustomUserForm

urlpatterns = [
    path('user/', UserCreateListView.as_view(), name='profiles'),
    path('user/<int:pk>', UserDetailView.as_view(), name='profile'),

]
