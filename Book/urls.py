from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from tornado.web import url

from Book import views
#
from Book.models import Category
from djangochannelsrestframework.consumers import view_as_consumer
# from .views import BookListView

# application = ProtocolTypeRouter({
#     "websocket": AuthMiddlewareStack(
#         URLRouter([
#             url(r"^front(end)/$", view_as_consumer(views)),
#         ])
#     ),
#  })

urlpatterns = [
    # path('books/', views.book_list),
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>', views.BookDetailView.as_view()),
    # path('books/<int:pk>', views.book_detail),
    path('category/', views.CategoryListView.as_view()),
    # path('category/', views.category_list),
    path('category/<int:pk>', views.CategoryDetailView.as_view()),
    # path('category/<int:pk>', views.category_detail),
]
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# # router.register(r'users', views.UserViewSet)
# router.register(r'users', views.UserDetailViewSet)
