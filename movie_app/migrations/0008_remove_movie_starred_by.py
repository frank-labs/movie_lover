# Generated by Django 5.1.3 on 2024-12-04 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_movie_starred_by_movie_watch_later_by_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='starred_by',
        ),
    ]