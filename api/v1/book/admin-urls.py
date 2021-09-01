from django.urls import path

# from apps.book.views import *
# #
# # from .views import BookListView
from api.v1.book.views import *

urlpatterns = [
    # path('books/', views.book_list),
    path('books/', BookListAdminView.as_view()),
    path('books/<int:pk>', BookDetailAdminView.as_view()),
    path('category/', CategoryListAdminView.as_view()),
    path('category/<int:pk>', CategoryDetailAdminView.as_view()),

]
