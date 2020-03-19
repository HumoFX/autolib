from django.urls import path
from Apps.University import views

urlpatterns = [
    path('university/', views.university_list),
    path('university/<int:pk>', views.university_detail),

]