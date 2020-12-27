from django.urls import path
from api.v1.Order import views

urlpatterns = [
    path('orders/', views.OrderListAdminView.as_view()),
    path('orders/short/', views.OrderShortListAdminView.as_view()),
    path('orders/create/', views.OrderCreateAdminView.as_view()),
    path('active_orders/', views.ActiveOrderListAdminView.as_view()),
    path('active_orders/<int:order_id>/', views.ActiveOrderDetailAdminView.as_view()),
    path('book_in_use/', views.BookInUseListAdminView.as_view()),
    path('book_in_use/<int:order_id>/', views.BookInUseDetailAdminView.as_view()),
    path('stats_per_day/', views.StatsPerDay.as_view()),
    path('stats_per_week/', views.StatsPerWeek.as_view()),
    path('stats_per_month/', views.StatsPerMonth.as_view()),
    path('stats_per_year/', views.StatsPerYear.as_view()),
    path('orders/<int:pk>/', views.OrderDetailView.as_view()),
]