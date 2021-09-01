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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from controlcenter.views import controlcenter


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('user/', include('apps.user.urls')),
    path('book/', include('apps.book.urls')),
    # sentry_sdk
    path('sentry-debug/', trigger_error),

    path('api/v1/client/', include('api.client.urls')),
    path('api/v1/admin/', include('api.admin.urls')),
    # path to djoser end points
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # path to our account's app endpoints
    path('auth/', include('djoser.urls')),
    path('admin/', admin.site.urls),
    path('datawizard/', include('data_wizard.urls')),
    path('admin/dashboard/', controlcenter.urls),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications of user')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
