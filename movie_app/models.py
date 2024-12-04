from django.db import models
from django.contrib.auth.models import User
import json

class Movie(models.Model):
    id = models.BigIntegerField(primary_key=True)  # ID from the API, not auto-incremented
    url = models.URLField(max_length=400,blank=True)  # URL to the movie's page
    imdb_code = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    title_english = models.CharField(max_length=255, blank=True, null=True)
    title_long = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)  # Runtime in minutes
    genres = models.JSONField(blank=True, null=True)  # Store genres as JSON
    summary = models.TextField(blank=True, null=True)  # Long text
    description_full = models.TextField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    yt_trailer_code = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    mpa_rating = models.CharField(max_length=255, blank=True, null=True)
    background_image = models.URLField(max_length=400, blank=True, null=True)
    background_image_original = models.URLField(max_length=400,blank=True, null=True)
    small_cover_image = models.URLField(max_length=400,blank=True, null=True)
    medium_cover_image = models.URLField(max_length=400,blank=True, null=True)
    large_cover_image = models.URLField(max_length=400,blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True, default='ok')
    torrents = models.JSONField(blank=True, null=True)  # Store torrents as JSON
    date_uploaded = models.DateTimeField(blank=True, null=True)  # Date uploaded
    date_uploaded_unix = models.BigIntegerField(blank=True, null=True)  # Unix timestamp for upload time
    watch_later_by = models.ManyToManyField(User, related_name='watch_later_movies', blank=True)

    class Meta:
        db_table = 'movies'  # Specifies that this model maps to the 'movies' table
        indexes = [
        models.Index(fields=['slug']),
        models.Index(fields=['imdb_code']),
        models.Index(fields=['title']),
        models.Index(fields=['title_english']), 
        models.Index(fields=['title_long']),
        models.Index(fields=['year']),
        models.Index(fields=['runtime']),
        models.Index(fields=['rating']),
        models.Index(fields=['date_uploaded']),
        models.Index(fields=['date_uploaded_unix']),
        models.Index(fields=['language']),
        ]

    def __str__(self):
        return self.title if self.title else "Unnamed Movie"
class Collection(models.Model):
    user = models.ForeignKey(User, related_name='collections', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    movies = models.ManyToManyField(Movie, related_name='collections', blank=True)

    def __str__(self):
        return f"Collection: {self.name} by {self.user.username}"
# class MovieAdmin(admin.ModelAdmin):
#     search_fields = ['title', 'imdb_code', 'slug']
#     list_filter = ['year', 'rating']
#     list_display = ['title', 'year', 'rating']