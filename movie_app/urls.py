from django.urls import path
from .views import CollectionCreateView, CollectionListView, CollectionDetailView, toggle_watch_later

from . import views
# app_name = 'movie_app' 
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('create/', CollectionCreateView.as_view(), name='create_collection'),
    path('collections/', CollectionListView.as_view(), name='collection_list'),  # List collections
    path('collections/<int:pk>/', CollectionDetailView.as_view(), name='collection_detail'),  
    path('toggle-watch-later/<int:movie_id>/', toggle_watch_later, name='toggle_watch_later'),
    path('watch-later/', views.WatchLaterView.as_view(), name='watch_later'),
    path('movies/genre/<str:genre_name>/', views.IndexView.as_view(), name='movies_by_genre'),  # Genre-based movie listing
]