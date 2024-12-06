from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import F, Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import CollectionForm
from .models import Movie
from django.shortcuts import render
from django.views import generic
from .models import Movie,Collection
import logging
from django.db.models import OuterRef, Subquery, IntegerField, Max, F, JSONField
from .forms import CollectionForm
# Get a logger instance
logger = logging.getLogger(__name__)
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie,Genre
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):
    model = Movie
    template_name = "movie_app/index.html"
    context_object_name = "movies"  # Optional: to customize the context name for the list of movies
    paginate_by = 40  # Set number of movies per page

    # This method allows sorting by different properties
    def get_queryset(self):
        # Start with all movies
        queryset = Movie.objects.all().order_by('-date_uploaded')

        # Filter by genre if a genre is specified in the URL
        genre_name = self.kwargs.get('genre_name')
        if genre_name:
            genre = get_object_or_404(Genre, name=genre_name)
            queryset = queryset.filter(genres=genre)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = context['page_obj']
        current_page = page_obj.number

        # Determine the range for previous and next pages
        previous_pages = [num for num in page_obj.paginator.page_range if num < current_page and current_page - num <= 3]
        next_pages = [num for num in page_obj.paginator.page_range if num > current_page and num - current_page <= 3]

        # Add them to the context
        context['previous_pages'] = previous_pages
        context['next_pages'] = next_pages
        
        # Optionally pass the genre filter
        genre_name = self.kwargs.get('genre_name')
        if genre_name:
            context['genre'] = get_object_or_404(Genre, name=genre_name)

        return context

class DetailView(generic.DetailView):
    model = Movie
    template_name = "movie_app/detail.html"

    def get_context_data(self, **kwargs):
        # Get the default context data (including the `movie` object)
        context = super().get_context_data(**kwargs)
        
        # Get the current movie ID
        current_movie_id = self.object.id
        
        # Get 22 movies with IDs near the current movie's ID
        suggested_movies = Movie.objects.filter(
            Q(id__lt=current_movie_id + 50, id__gt=current_movie_id - 50) & ~Q(id=current_movie_id)
        ).order_by('id')[:22]
        
        # Add suggested movies to the context
        context['suggested_movies'] = suggested_movies
        # Check if the current movie is in the user's "watch later" list
        if self.request.user.is_authenticated:
            context['is_watch_later'] = self.object in self.request.user.watch_later_movies.all()
        else:
            context['is_watch_later'] = False
        
        return context

class CollectionListView(generic.ListView):
    model = Collection
    template_name = 'movie_app/collections_list.html'
    context_object_name = 'collections'
    
    def get_queryset(self):
        # Filter collections by the logged-in user
        return Collection.objects.filter(user=self.request.user)

class CollectionDetailView(generic.DetailView):
    model = Collection
    template_name = 'movie_app/collection_detail.html'
    context_object_name = 'collection'

    def get_queryset(self):
        # Ensure the collection belongs to the logged-in user
        return Collection.objects.filter(user=self.request.user)

class CollectionCreateView(generic.CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'movie_app/create_collection.html'
    success_url = reverse_lazy('collection_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the current user
        return super().form_valid(form)
    
@login_required
def toggle_watch_later(request, movie_id):
    """
    Toggle the watch later status for the given movie and the current user.
    """
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user

    if movie in user.watch_later_movies.all():
        user.watch_later_movies.remove(movie)
        added = False
    else:
        user.watch_later_movies.add(movie)
        added = True

    return JsonResponse({'added': added})

class WatchLaterView(LoginRequiredMixin, generic.ListView):
    template_name = "movie_app/index.html"  # Reuse the IndexView template
    context_object_name = "movies"
    paginate_by = 10  # Optional: Add pagination if necessary

    def get_queryset(self):
        """
        Filter movies that the current user has added to their 'Watch Later' list.
        """
        return self.request.user.watch_later_movies.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_watch_later_view'] = True  # Pass the flag to the template
        return context
    
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
class RemoveWatchLaterView(LoginRequiredMixin, View):
    def post(self, request, movie_id):
        """
        Remove the movie from the user's Watch Later list.
        """
        try:
            movie = request.user.watch_later_movies.get(pk=movie_id)
            request.user.watch_later_movies.remove(movie)
            return JsonResponse({"success": True})
        except:
            return JsonResponse({"success": False}, status=400)
    