from django.urls import path
from tornado.web import url

from .views import *

app_name = 'book'
urlpatterns = [
    path('list/', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail')
]
