from rest_framework import serializers

from movies_app.models import *


# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = '__all__'
#         depth = 1

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = ['id', 'name', 'release_year']
        exclude = ['actors', 'description']


class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['actors']