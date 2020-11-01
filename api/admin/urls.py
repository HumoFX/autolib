from django.urls import path, include

urlpatterns = [
    path('', include('api.v1.Book.admin-urls')),
    path('', include('api.v1.User.admin-urls')),
    path('', include('api.v1.University.admin-urls')),
    path('', include('api.v1.Order.admin-urls')),
]
