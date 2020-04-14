from django.urls import path
from Book import views
#
urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>', views.book_detail),
    path('category/', views.category_list),
    path('category/<int:pk>', views.category_detail),
]
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# # router.register(r'users', views.UserViewSet)
# router.register(r'users', views.UserDetailViewSet)
