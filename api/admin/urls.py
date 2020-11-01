from django.urls import path, include
from api.v1.User.views import RefreshTokenView, ObtainTokenPairView


urlpatterns = [
    path('', include('api.v1.Book.admin-urls')),
    path('', include('api.v1.User.admin-urls')),
    path('', include('api.v1.University.admin-urls')),
    path('', include('api.v1.Order.admin-urls')),
    path('token/', ObtainTokenPairView.as_view(), name='get tokens'),
    path('token/refresh/', RefreshTokenView.as_view(), name='update tokens')
]
