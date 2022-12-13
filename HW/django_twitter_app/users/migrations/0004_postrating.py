from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181020_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.IntegerField(default=1),
        ),
    ]