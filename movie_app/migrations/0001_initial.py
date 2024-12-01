# Generated by Django 5.1.3 on 2024-12-01 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('imdb_code', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=255)),
                ('title_english', models.CharField(max_length=255)),
                ('title_long', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
                ('runtime', models.IntegerField()),
                ('genres', models.JSONField()),
                ('summary', models.TextField(blank=True, null=True)),
                ('description_full', models.TextField(blank=True, null=True)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('yt_trailer_code', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=20)),
                ('mpa_rating', models.CharField(blank=True, max_length=20, null=True)),
                ('background_image', models.URLField()),
                ('background_image_original', models.URLField()),
                ('small_cover_image', models.URLField()),
                ('medium_cover_image', models.URLField()),
                ('large_cover_image', models.URLField()),
                ('state', models.CharField(max_length=20)),
                ('torrents', models.JSONField()),
                ('date_uploaded', models.DateTimeField()),
                ('date_uploaded_unix', models.BigIntegerField()),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]
