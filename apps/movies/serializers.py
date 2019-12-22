from rest_framework import serializers
from movies.models import Movie, MovieGenres


class MovieSerializer(serializers.ModelSerializer):
    """电影序列化"""

    class Meta:
        model = Movie
        fields = "__all__"


class MovieGenresSerializer(serializers.ModelSerializer):
    """电影流派枚举序列化"""

    class Meta:
        model = MovieGenres
        fields = "__all__"
