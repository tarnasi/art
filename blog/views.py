from rest_framework.viewsets import generics 

from .serializers import *
from .models import Post
from django.contrib.auth.models import User


class PostListViewSet(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveViewSet(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        user_id = self.request.POST.get('user_id')
        user = User.objects.get(pk=user_id)
        serializer.save(user=user)
