import pickle
from typing import Dict, Tuple
import sys

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from movies.models import Movie
from movies.serializers import MovieSerializer


class MoviePagination(PageNumberPagination):
    """电影分页"""
    page_size = 10  # 每页显示数据条数
    page_query_param = 'page'  # 哪一页
    page_size_query_param = 'page_size'  # 用于调整每页显示条数
    max_page_size = 20  # 最大的每页显示数据条数


class MovieViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """电影信息ViewSet"""
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    queryset = Movie.objects.all()

    search_fields = ('title', 'mean_rate')
    ordering_fields = ('mean_rate',)

    # 设置排序规则
    ordering = ('id',)
