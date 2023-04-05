from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django_api import models


# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Posts
        fields = "__all__"  # ['id', 'title']
        # fields = ['id']