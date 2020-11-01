from ajax_select import urls as ajax_select_urls
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    url(r'^ajax_select/', include(ajax_select_urls)),
    path('', include('api.v1.Book.urls')),
    path('', include('api.v1.User.urls')),
    path('', include('api.v1.University.urls')),
    path('', include('api.v1.Order.urls')),
]
