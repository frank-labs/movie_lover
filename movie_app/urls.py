from django.urls import path
from .views import (CollectionCreateView, CollectionListView, CollectionDetailView, toggle_watch_later,RemoveWatchLaterView,WatchLaterView,UpdateCollectionView,DeleteCollectionView,add_to_collections)

from . import views
# app_name = 'movie_app' 
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('search/', views.search, name='search'),
    path('create/', CollectionCreateView.as_view(), name='create_collection'),
    path('collections/', CollectionListView.as_view(), name='collection_list'),  # List collections
    path('collections/<int:pk>/', CollectionDetailView.as_view(), name='collection_detail'), 
    path("collections/update/<int:pk>/", UpdateCollectionView.as_view(), name="update_collection"),
    path("collections/delete/<int:pk>/", DeleteCollectionView.as_view(), name="delete_collection"),
    path('toggle-watch-later/<int:movie_id>/', toggle_watch_later, name='toggle_watch_later'),
    path("watch-later/", WatchLaterView.as_view(), name="watch_later"),
    path("watch-later/remove/<int:movie_id>/", RemoveWatchLaterView.as_view(), name="remove_watch_later"),
    path('movies/genre/<str:genre_name>/', views.IndexView.as_view(), name='movies_by_genre'),  # Genre-based movie listing
    path('add-to-collections/', add_to_collections, name='add_to_collections'),
    path('dmca-disclaimer/', views.dmca_disclaimer, name='dmca_disclaimer'),
]