from ajax_select import urls as ajax_select_urls
from django.urls import path, include
from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    url(r'^ajax_select/', include(ajax_select_urls)),
    path('', include('api.v1.Book.urls')),
    path('', include('api.v1.User.urls')),
    path('', include('api.v1.University.urls')),
    path('', include('api.v1.Order.urls')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
