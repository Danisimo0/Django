from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_twitter_app', '0002_post_user_alter_post_description_alter_post_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='article',
            field=models.ForeignKey(blank=True, default=None, help_text='<small class="text-muted">ForeignKey</small><hr><br>', null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_twitter_app.post', verbose_name='Статья'),
        ),
    ]