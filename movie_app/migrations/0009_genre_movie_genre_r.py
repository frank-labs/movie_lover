# Generated by Django 5.1.3 on 2024-12-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_remove_movie_starred_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_r',
            field=models.ManyToManyField(to='movie_app.genre'),
        ),
    ]
