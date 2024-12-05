from movie_app.models import Genre

def genres_context(request):
    """
    Add the list of unique genres to the context.
    """
    # Get all unique genres by using the Genre model
    genres = Genre.objects.all().distinct()  # Get unique genres
    return {
        'genres': genres
    }