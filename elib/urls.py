"""elib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import notifications.urls
from ajax_select import urls as ajax_select_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django_registration.backends.activation.views import RegistrationView
from rest_framework_simplejwt import views as jwt_views

from Book import views
from User.forms import MyCustomUserForm

urlpatterns = [
    url(r'^ajax_select/', include(ajax_select_urls)),
    path('', include('Book.urls')),
    path('', include('User.urls')),
    path('', include('University.urls')),
    path('', include('Order.urls')),

    # path to djoser end points
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # path to our account's app endpoints
    path('api/accounts/', include("User.urls")),
    # url(r'^admin_tools/', include('admin_tools.urls')),
    path('admin/', admin.site.urls),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
