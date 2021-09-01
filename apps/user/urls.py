from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path, include

from .views import  IndexView
app_name = 'user'
urlpatterns = [
    path('', IndexView.as_view(template_name='librarian/index.html'), name='index'),
    path('login/', LoginView.as_view(template_name='librarian/login.html'), name='login'),
]
