import pickle
from typing import Dict, Tuple
import sys

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status


class MovieViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = set()
    movies = None

    def retrieve(self, request, *args, **kwargs):
        movie_id = int(kwargs['pk'])
        if self.movies is None:
            with open('./Jupyter/movie.pkl', 'rb') as f:
                self.movies: Dict = pickle.load(f)
        movie_msg = dict() if movie_id not in self.movies else self.movies[movie_id]
        return Response(movie_msg, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        return Response({'ok': 1}, status=status.HTTP_200_OK)
