from django.urls import path
from django.conf import settings
from .views import *

app_name = 'blog'
urlpatterns = [
    path('posts', PostListViewSet.as_view(), name="post-list"),
    path('posts/<int:pk>', PostRetrieveViewSet.as_view(), name="post-detail"),
    path('posts/create', PostCreateViewSet.as_view(), name="post-create"),
    # path('blogs/<pk:int>/edit', ),
    # path('blogs/<pk:int>/delete', ),
]
