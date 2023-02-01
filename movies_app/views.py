from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies_app.models import *
from movies_app.serializers import *


# Create your views here.

@api_view(['GET'])
def movies_list(request):
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


# @api_view(['GET'])
# def movie_details(request, movie_id: int):
#     try:
#         movie = Movie.objects.get(id=movie_id)
#         serializer = MovieDetailsSerializer(movie, many=False)
#         return Response(serializer.data)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def movie_details(request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieDetailsSerializer(movie, many=False)
    return Response(serializer.data)

