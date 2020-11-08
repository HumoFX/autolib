from django.urls import path
from .views import *

urlpatterns = [
    path('university/', UniversityListView.as_view()),
    path('faculty/', FacultyListView.as_view()),
]