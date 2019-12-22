import pickle
from typing import Dict, Tuple
import sys

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from movies.models import Movie, MovieGenres
from movies.serializers import MovieSerializer, MovieGenresSerializer


class MoviePagination(PageNumberPagination):
    """电影分页"""
    page_size = 10  # 每页显示数据条数
    page_query_param = 'page'  # 哪一页
    page_size_query_param = 'page_size'  # 用于调整每页显示条数
    max_page_size = 20  # 最大的每页显示数据条数


# 这个接口可能用不上
class MovieViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """电影信息ViewSet"""
    serializer_class = MovieSerializer
    # pagination_class = MoviePagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    queryset = Movie.objects.all()

    # 这里只按流派查询，但这里是个全文搜索，就先这样用
    # http://localhost:8000/movie/?search=Adventure
    search_fields = ('genres',)

    # 排序允许按mean_rate排序
    ordering_fields = ('mean_rate',)

    # 设置排序规则
    ordering = ('id',)


class MovieGenresViewSet(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """电影流派枚举序列化"""
    serializer_class = MovieGenresSerializer
    queryset = MovieGenres.objects.all()

