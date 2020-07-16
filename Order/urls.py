from django.urls import path
from Order import views

urlpatterns = [
    path('orders/', views.OrderListView.as_view()),
    path('orders/<int:pk>', views.order_detail),
    path('book_in_use/', views.book_inuse_list),
    path('book_in_use/<int:pk>', views.book_inuse_detail),
]