from django.urls import path
from Apps.Book import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>', views.book_detail),
    path('category/', views.category_list),
    path('category/<int:pk>', views.category_detail),
]