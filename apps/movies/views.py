import pickle
from typing import Dict, Tuple
import sys

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class MoviePagination(PageNumberPagination):
    """电影分页"""
    page_size = 10  # 每页显示数据条数
    page_query_param = 'p'  # 哪一页
    page_size_query_param = 'size'  # 用于调整每页显示条数
    max_page_size = 20  # 最大的每页显示数据条数


class MovieViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """电影信息ViewSet"""
    queryset = set()
    movies = None
    pagination_class = MoviePagination

    def retrieve(self, request, *args, **kwargs):
        movie_id = int(kwargs['pk'])
        if self.movies is None:
            with open('./Jupyter/movie.pkl', 'rb') as f:
                self.movies: Dict = pickle.load(f)
        movie_msg = dict() if movie_id not in self.movies else self.movies[movie_id]
        return Response(movie_msg, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        return Response({'ok': 1}, status=status.HTTP_200_OK)
