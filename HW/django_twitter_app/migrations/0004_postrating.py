from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_twitter_app', '0003_postcomment_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(blank=True, default=False, verbose_name='Статус')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='<small class="text-muted">DateTimeField</small><hr><br>', null=True, verbose_name='Дата и время создания')),
                ('article', models.ForeignKey(blank=True, default=None, help_text='<small class="text-muted">ForeignKey</small><hr><br>', null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_twitter_app.post', verbose_name='Статья')),
                ('user', models.ForeignKey(blank=True, default=None, help_text='<small class="text-muted">ForeignKey</small><hr><br>', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Рейтинг публикации',
                'verbose_name_plural': 'Рейтинги публикаций',
                'ordering': ('-created',),
            },
        ),
    ]