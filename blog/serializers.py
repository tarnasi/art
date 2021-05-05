from django.contrib.auth.models import User
from .models import Post
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user', 'photo']
        read_only_fields = ['created_at']

