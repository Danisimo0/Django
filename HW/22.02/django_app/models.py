from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):


    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    title = models.CharField(
        db_column='title_db_column',
        db_index=True,
        db_tablespace='title_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Заголовок',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',

        max_length=300,
    )
    description = models.TextField(
        db_column='description_db_column',
        db_index=True,
        db_tablespace='description_db_tablespace',
        error_messages=False,
        primary_key=False,
        validators=[MinLengthValidator(0), MaxLengthValidator(3000), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name='Описание',
        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',

        max_length=3000,
    )
    is_completed = models.BooleanField(
        db_column='is_completed_db_column',
        db_index=True,
        db_tablespace='is_completed_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=False,
        verbose_name='Статус выполнения',
        help_text='<small class="text-muted">BooleanField</small><hr><br>',
    )
    created = models.DateTimeField(
        db_column='created_db_column',
        db_index=True,
        db_tablespace='created_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время создания',
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',

        auto_now=False,
        auto_now_add=False,
    )
    updated = models.DateTimeField(
        db_column='updated_db_column',
        db_index=True,
        db_tablespace='updated_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время обновления',
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',

        auto_now=False,
        auto_now_add=False,
    )


    class Meta:
        app_label = 'app_django'
        ordering = ('-updated',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        db_table = 'task_task_list_model_table'

    def __str__(self):
        if self.is_completed:
            completed = "Активно"
        else:
            completed = "Неактивно"
        return f"{self.title} | {self.description[0:30]}... | {completed} | {self.updated}"


class Post(models.Model):
    """
     Post
    """
    title = models.CharField(
        verbose_name="Заголовок",
        default="",
        editable=True,
        blank=True,
        unique=True,
        db_index=True,

        max_length=150
    )
    description = models.TextField(
        verbose_name="Описание",
        default="",
        editable=True,
        blank=True
    )

    class Meta:
        app_label = 'app_django'
        ordering = ('id',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'task_post_list_model_table'

    def __str__(self):
        return f"Post: {self.title} {self.description[:30]} [{self.pk}]"


class PostComment(models.Model):
    """
     Post Comment
    """
    user = models.ForeignKey(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=User,
        on_delete=models.SET_NULL,
    )
    article = models.ForeignKey(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Статья',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=Post,
        on_delete=models.SET_NULL,
    )
    text = models.CharField(
        verbose_name="Текст комментария",
        default="",
        editable=True,
        blank=True,
        unique=False,
        db_index=False,

        max_length=300
    )
    created = models.DateTimeField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время создания',
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',

        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        app_label = 'app_django'
        ordering = ('-created',)
        verbose_name = 'Комментарий к публикации'
        verbose_name_plural = 'Комментарии к публикациям'
        db_table = 'task_post_comment_model_table'

    def __str__(self):
        return f"PostComment: {self.user} {self.text[:30]} [{self.created}]"