# Generated by Django 4.1.7 on 2023-03-06 13:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-publication_date', 'title'],
            },
        ),
    ]
