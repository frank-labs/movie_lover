from django.shortcuts import render

from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Movie
from django.shortcuts import render
from django.views import generic
from .models import Movie
import logging

# Get a logger instance
logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    model = Movie
    template_name = "movie_app/index.html"
    context_object_name = "movies"  # Optional: to customize the context name for the list of movies
    paginate_by = 10  # Set number of movies per page

    # This method allows sorting by different properties
    def get_queryset(self):
        # Get the base queryset
        queryset = Movie.objects.all()

        # Get the sort parameter from the URL (default to 'date_uploaded' if not provided)
        sort_by = self.request.GET.get('sort_by', 'date_uploaded')

        # Add sorting based on the 'sort_by' query parameter
        if sort_by in ['date_uploaded', 'rating', 'year']:  # Limit sorting to valid fields
            queryset = queryset.order_by(sort_by)
        else:
            queryset = queryset.order_by('date_uploaded')  # Default sorting
        # print("Queryset before returning:", queryset)
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
        return context

class DetailView(generic.DetailView):
    model = Movie
    template_name = "movie_app/detail.html"