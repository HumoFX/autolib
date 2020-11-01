from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from tornado.web import url

from .views import *
#
from .models import Category
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
    path('books/', BookListView.as_view()),
    path('books/<int:pk>', BookDetailView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>', CategoryDetailView.as_view()),

]
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# # router.register(r'users', views.UserViewSet)
# router.register(r'users', views.UserDetailViewSet)
