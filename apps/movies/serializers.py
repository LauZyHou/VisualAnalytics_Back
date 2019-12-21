from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """电影序列化"""

    class Meta:
        model = Movie
        fields = "__all__"
