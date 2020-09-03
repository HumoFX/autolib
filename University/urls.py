from django.urls import path
from University import views

urlpatterns = [
    path('university/', views.UniversityListView.as_view()),
    # path('university/<int:pk>', views.UniversityListView.as_view()),
    path('faculty/', views.FacultyListView.as_view()),
]