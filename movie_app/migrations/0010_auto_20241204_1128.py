# Generated by Django 5.1.3 on 2024-12-04 16:28

from django.db import migrations

def populate_genres(apps, schema_editor):
    Movie = apps.get_model('movie_app', 'Movie')
    Genre = apps.get_model('movie_app', 'Genre')

    # Step 1: Create Genre objects for all unique genres
    print("Step 1: Collecting unique genres...")
    unique_genres = set()
    movies = Movie.objects.all()
    movie_count = movies.count()
    print(f"Found {movie_count} movies to process.")

    for index, movie in enumerate(movies, start=1):
        if movie.genres:  # Ensure the genres JSON field is not empty
            unique_genres.update(movie.genres)  # Add all genres to the set
        if index % 100 == 0:  # Show progress every 100 movies
            print(f"Processed {index}/{movie_count} movies for unique genres.")

    print(f"Step 1 complete: Found {len(unique_genres)} unique genres.")

    # # Step 2: Create Genre entries in the database
    # print("Step 2: Creating Genre entries...")
    # for genre_index, genre_name in enumerate(unique_genres, start=1):
    #     Genre.objects.get_or_create(name=genre_name)
    #     if genre_index % 50 == 0:  # Show progress every 50 genres
    #         print(f"Created {genre_index}/{len(unique_genres)} genres.")

    # print("Step 2 complete: Genres created.")

    # Step 3: Associate Movie objects with Genre objects
    print("Step 3: Associating movies with genres...")
    for index, movie in enumerate(movies, start=1):
        if movie.genres:
            # Get or create Genre objects for the movie's genres
            genres = Genre.objects.filter(name__in=movie.genres)
            # Add these Genre objects to the movie's genre_r ManyToManyField
            movie.genre_r.set(genres)
            movie.save()
        if index % 100 == 0:  # Show progress every 100 movies
            print(f"Associated {index}/{movie_count} movies with genres.")

    print("Step 3 complete: Movies associated with genres.")


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('movie_app', '0009_genre_movie_genre_r'),
    ]

    operations = [
        migrations.RunPython(populate_genres),
    ]