from django.urls import path
from tornado.web import url

from .views import *


urlpatterns = [
    # path('books/', views.book_list),
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('category/<int:category_id>/books/', BookCategoryDetailView.as_view()),
    path('udc/list/', UDCListAPIView.as_view()),
    path('udc/<int:id>/', UDCChildrenListAPIView.as_view()),
    path('udc/<udc_id>/books/', BookUDCListAPIView.as_view()),
    path('file/', custom_upload_csv)

]
