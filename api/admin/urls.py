from django.urls import path, include
# from apps.user.views import RefreshTokenView, ObtainTokenPairView


urlpatterns = [
    path('', include('api.v1.book.admin-urls')),
    path('', include('api.v1.user.admin-urls')),
    path('', include('api.v1.university.admin-urls')),
    path('', include('api.v1.order.admin-urls')),
    # path('token/', ObtainTokenPairView.as_view(), name='get tokens'),
    # path('token/refresh/', RefreshTokenView.as_view(), name='update tokens')
]
