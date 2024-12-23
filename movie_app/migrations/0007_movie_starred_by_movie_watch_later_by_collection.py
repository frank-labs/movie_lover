# Generated by Django 5.1.3 on 2024-12-02 21:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_alter_movie_background_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='starred_by',
            field=models.ManyToManyField(blank=True, related_name='starred_movies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='watch_later_by',
            field=models.ManyToManyField(blank=True, related_name='watch_later_movies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('movies', models.ManyToManyField(blank=True, related_name='collections', to='movie_app.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
