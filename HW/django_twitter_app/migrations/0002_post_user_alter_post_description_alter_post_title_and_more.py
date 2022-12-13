from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_twitter_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, default=None, help_text='<small class="text-muted">ForeignKey</small><hr><br>', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, db_index=True, default='', max_length=150, unique=True, verbose_name='Заголовок'),
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default='', max_length=300, verbose_name='Текст комментария')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='<small class="text-muted">DateTimeField</small><hr><br>', null=True, verbose_name='Дата и время создания')),
                ('user', models.ForeignKey(blank=True, default=None, help_text='<small class="text-muted">ForeignKey</small><hr><br>', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий к публикации',
                'verbose_name_plural': 'Комментарии к публикациям',
                'ordering': ('-created',),
            },
        ),
    ]