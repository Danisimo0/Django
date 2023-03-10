from django.db import models
from rest_framework import serializers


class Posts(models.Model):
    user_id = models.PositiveIntegerField(default=1)

    title = models.CharField(max_length=300)
    title = models.TextField()
    completed = models.BooleanField(default=False)

    # created = models.DateTimeField()
    # update = models.DateTimeField()

    class Meta:
        app_label = 'django_api'
        ordering = ('id',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['title']