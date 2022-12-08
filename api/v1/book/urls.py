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
    path('file/', custom_upload_csv),
    path('labels/', BookLabelingExportView.as_view()),
    path('userlabels/export/', UserLabelingExportView.as_view()),
    path('userlabels/', UserLabelListView.as_view()),
    path('labels/update/', LabelsUpdateApiView.as_view()),
    path('userlabels/update/', UserLabelsUpdateApiView.as_view()),
    path('labels/<str:id>/', LabelIdentifyAPIView.as_view()),
    path('userlabels/<str:id>/', UserLabelIdentifyAPIView.as_view()),

    # REWRITING VIEWS
]