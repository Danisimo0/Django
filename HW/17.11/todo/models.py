from django.db import models

# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    list_display_links = None

    user_nickname = models.CharField(
        verbose_name="user_nickname",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )
    user_password = models.CharField(
        verbose_name="user_password",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )

    class Meta:
        app_label = 'twitter_app'
        ordering = ('id',)
        verbose_name = 'Users'
        verbose_name_plural = 'Users'




class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    list_display_links = None
    author_id = models.IntegerField(
        verbose_name="author_id",
        default=0,
        editable=True,
        blank=True,
    )
    title = models.CharField(
        verbose_name="title",
        default="",
        editable=True,
        blank=True,
        max_length=300
    )
    description = models.CharField(
        verbose_name="description",
        default="",
        editable=True,
        blank=True,
        max_length=300
    )

    class Meta:
        app_label = 'twitter_app'
        ordering = ('id',)
        verbose_name = 'Tasks'
        verbose_name_plural = 'Tasks'
