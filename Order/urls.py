from django.urls import path
from Order import views

urlpatterns = [
    path('orders/', views.OrderListView.as_view()),
    path('active_orders/', views.ActiveOrderListView.as_view()),
    path('active_orders/<int:id>', views.ActiveOrderDetailView.as_view()),
    path('book_in_use/', views.BookInUseListView.as_view()),
    path('book_in_use/<int:id>', views.BookInUseDetailView.as_view()),
    path('stats_per_day/', views.StatsPerDay.as_view()),
    path('stats_per_week/', views.StatsPerWeek.as_view()),
    path('stats_per_month/', views.StatsPerMonth.as_view()),
    path('stats_per_year/', views.StatsPerYear.as_view()),
    path('orders/<int:pk>', views.OrderDetailView.as_view()),
    # path('book_in_use/', views.BookInUseListView.as_view()),
    # path('book_in_use/<int:pk>', views.BookInUseDetailView.as_view()),
]