from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from movies_app.models import *
from movies_app.serializers import *


# Create your views here.

def get_movies_list(request):
    movies_qs = Movie.objects.all()

    if 'name' in request.query_params:
        movies_qs = movies_qs.filter(name__iexact=request.query_params['name'])
    if 'duration_from' in request.query_params:
        movies_qs = movies_qs.filter(duration_in_min__gte=request.query_params['duration_from'])
    if 'duration_to' in request.query_params:
        movies_qs = movies_qs.filter(duration_in_min__lte=request.query_params['duration_to'])
    if 'description' in request.query_params:
        movies_qs = movies_qs.filter(description__icontains=request.query_params['description'])

    if not movies_qs:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = MovieSerializer(movies_qs, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def movies_list(request):
    if request.method == 'GET':
        return get_movies_list(request)
    elif request.method == 'POST':
        serializer = MovieDetailsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def movie_details(request, movie_id: int):
#     try:
#         movie = Movie.objects.get(id=movie_id)
#         serializer = MovieDetailsSerializer(movie, many=False)
#         return Response(serializer.data)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PATCH'])
def movie_details(request: Request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'GET':
        serializer = MovieDetailsSerializer(movie, many=False)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = MovieDetailsSerializer(
            movie, data=request.data, many=False, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)
@api_view(['GET', 'POST'])
def movie_actors(request, movie_id):
    if request.method == 'GET':
        movie_actors = MovieActor.objects.filter(movie_id=movie_id)
        serializer = MovieActorSerializer(movie_actors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        get_object_or_404(Movie, id=movie_id)
        serializer = AddMovieActorSerializer(data=request.data,
                                             context={'movie_id': movie_id, 'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response()


def index(request):
    return render(request, 'static/index.html')