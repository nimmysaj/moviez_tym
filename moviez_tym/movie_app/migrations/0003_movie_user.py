# Generated by Django 5.0.3 on 2024-03-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_alter_movie_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.CharField(default='qwe', max_length=200),
            preserve_default=False,
        ),
    ]