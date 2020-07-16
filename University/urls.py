from django.urls import path
from University import views

urlpatterns = [
    path('university/', views.university_list),
    path('university/<int:pk>', views.university_detail),

]