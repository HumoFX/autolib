from django.urls import path
from Book import views
#
from Book.models import Category

urlpatterns = [
    # path('books/', views.book_list),
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>', views.BookDetailView.as_view()),
    # path('books/<int:pk>', views.book_detail),
    path('category/', views.CategoryListView.as_view()),
    # path('category/', views.category_list),
    path('category/<int:pk>', views.CategoryDetailView.as_view()),
    # path('category/<int:pk>', views.category_detail),
]
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# # router.register(r'users', views.UserViewSet)
# router.register(r'users', views.UserDetailViewSet)
