from django.urls import path
from api.v1.Order import views

urlpatterns = [
    path('orders/', views.OrderListView.as_view()),
    path('orders/create/', views.OrderCreateView.as_view()),
    path('active_orders/', views.ActiveOrderListView.as_view()),
    path('active_orders/<int:order_id>', views.ActiveOrderDetailView.as_view()),
    path('book_in_use/', views.BookInUseListView.as_view()),
    path('book_in_use/<int:order_id>', views.BookInUseDetailView.as_view()),
    path('orders/<int:pk>', views.OrderDetailView.as_view()),
]