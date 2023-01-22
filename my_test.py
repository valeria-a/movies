import os
import django


os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()


from movies_app.models import Movie, Rating

# new_movie = Movie(movie_name="ccc", release_year=2021, duration_in_min=14)
# new_movie.save()
# new_movie = Movie(movie_name="ddd", release_year=2021, duration_in_min=14)
# new_movie.save()
# new_movie = Movie(movie_name="eee", release_year=2021, duration_in_min=14)
# new_movie.save()
# new_movie = Movie(movie_name="fff", release_year=2021, duration_in_min=14)
# new_movie.save()


# all_movies = Movie.objects.all()
# total_duration = 0
# for movie in all_movies:
#     total_duration += movie.duration_in_min
#
# print(total_duration)


# all_movies = Movie.objects.all()
# for movie in all_movies:
#     Rating(movie=movie, rating=9).save()


movie = Movie.objects.get(pk=3)
print(movie.rating_set.all())