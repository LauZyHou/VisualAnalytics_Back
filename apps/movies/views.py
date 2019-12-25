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

# 以下类外部分为实现静态代码功能

# 获取类别枚举列表
with open('./Jupyter/type_list.pkl', 'rb') as f:
    type_list = pickle.load(f)

# 获取地区枚举列表
with open('./Jupyter/zone_list.pkl', 'rb') as f:
    zone_list = pickle.load(f)

# 获取1925-2016年的平均score
with open('./DataSet/douban_more/mean_score_list.pkl', 'rb') as f:  # 世界
    mean_score_list = pickle.load(f)
with open('./DataSet/douban_more/mean_score_list_cn.pkl', 'rb') as f:  # 中国大陆
    mean_score_list_cn = pickle.load(f)

# 获取[0, 5, 6.5, 7.5, 8, 8.5, 9, 10]两两区间下的score分布
with open('./DataSet/douban_more/score_distri.pkl', 'rb') as f:  # 世界
    score_distri = pickle.load(f)
with open('./DataSet/douban_more/score_distri_cn.pkl', 'rb') as f:  # 中国大陆
    score_distri_cn = pickle.load(f)

# 获取1920-2016年的电影数目变化
with open('./DataSet/douban_more/mvnum_list.pkl', 'rb') as f:  # 世界
    mvnum_list = pickle.load(f)
with open('./DataSet/douban_more/mvnum_list_cn.pkl', 'rb') as f:  # 中国大陆
    mvnum_list_cn = pickle.load(f)

# 获取1920-2016年的评论数目变化
with open('./DataSet/douban_more/pnum_list.pkl', 'rb') as f:  # 世界
    pnum_list = pickle.load(f)
with open('./DataSet/douban_more/pnum_list_cn.pkl', 'rb') as f:  # 中国大陆
    pnum_list_cn = pickle.load(f)

# 获取2010-2016年五个区间评分的电影数目变化
with open('./DataSet/douban_more/score_flow.pkl', 'rb') as f:  # 世界
    score_flow = pickle.load(f)
with open('./DataSet/douban_more/score_flow_cn.pkl', 'rb') as f:  # 中国大陆
    score_flow_cn = pickle.load(f)

# 获取各个类型的最多四个导演信息
with open('./DataSet/douban_boutique/type_director_dict.pkl', 'rb') as f:
    type_director_dict = pickle.load(f)
# 获取各个地区的最多四个导演信息
with open('./DataSet/douban_boutique/zone_director_dict.pkl', 'rb') as f:
    zone_director_dict = pickle.load(f)

# 获取各个类型的score信息
with open('./DataSet/douban_boutique/type_score_dict.pkl', 'rb') as f:
    type_score_dict = pickle.load(f)

# 获取各个类型的account信息
with open('./DataSet/douban_boutique/type_account_dict2.pkl', 'rb') as f:
    type_account_dict = pickle.load(f)

# 获取各个地区的score信息
with open('./DataSet/douban_boutique/zone_score_dict.pkl', 'rb') as f:
    zone_score_dict = pickle.load(f)

# 获取各个类型的account信息
with open('./DataSet/douban_boutique/zone_account_dict.pkl', 'rb') as f:
    zone_account_dict = pickle.load(f)


class TypeViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """电影类别枚举，使用douban的boutique数据集，保存在type_set.pkl中"""
    queryset = set()

    def list(self, request, *args, **kwargs):
        return Response(type_list, status=status.HTTP_200_OK)


class ZoneViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """地区类别枚举"""
    queryset = set()

    def list(self, request, *args, **kwargs):
        return Response(zone_list, status=status.HTTP_200_OK)


class MeanScoreViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    """获取平均得分(世界&中国大陆)，这保存在pickle中"""
    queryset = set()

    def list(self, request, *args, **kwargs):
        return Response({"世界": mean_score_list,
                         "中国大陆": mean_score_list_cn}, status=status.HTTP_200_OK)


class ScoreDistributionViewSet(mixins.ListModelMixin,
                               viewsets.GenericViewSet):
    """获取得分的分布情况(世界&中国大陆)，这保存在pickle中"""
    queryset = set()

    def list(self, request, *args, **kwargs):
        return Response({"世界": score_distri,
                         "中国大陆": score_distri_cn}, status=status.HTTP_200_OK)


class MVAndPNumViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    """电影数目、评论数目随时间的变化(1920-2016)"""
    queryset = set()

    def list(self, request, *args, **kwargs):
        return Response({"电影数(世界)": mvnum_list,
                         "电影数(中国大陆)": mvnum_list_cn,
                         "评论数(世界)": pnum_list,
                         "评论数(中国大陆)": pnum_list_cn
                         }, status=status.HTTP_200_OK)


class ScoreFlowViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    """获取2010-2016年五个区间评分的电影数目变化"""
    queryset = set()

    def list(self, request, *args, **kwargs):
        return Response({"世界": score_flow,
                         "中国大陆": score_flow_cn},
                        status=status.HTTP_200_OK)


class TypeDirectorViewSet(mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """获取某个类型的最多四个导演信息"""
    queryset = set()

    def retrieve(self, request, *args, **kwargs):
        typestr = kwargs['pk']
        if typestr not in type_director_dict:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        return Response(type_director_dict[typestr], status=status.HTTP_200_OK)


class ZoneDirectorViewSet(mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """获取某个地区的最多四个导演信息"""
    queryset = set()

    def retrieve(self, request, *args, **kwargs):
        zonestr = kwargs['pk']
        if zonestr not in zone_director_dict:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        return Response(zone_director_dict[zonestr], status=status.HTTP_200_OK)


class TypeAccountViewSet(mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    """获取各个类型的account信息"""
    queryset = set()

    def retrieve(self, request, *args, **kwargs):
        typestr = kwargs['pk']
        if typestr not in type_account_dict:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        return Response(type_account_dict[typestr], status=status.HTTP_200_OK)


class TypeScoreViewSet(mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    """获取各个类型的score信息"""
    queryset = set()

    def retrieve(self, request, *args, **kwargs):
        typestr = kwargs['pk']
        if typestr not in type_score_dict:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        return Response(type_score_dict[typestr], status=status.HTTP_200_OK)


class ZoneAccountViewSet(mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    """获取各个类型的account信息"""
    queryset = set()

    def retrieve(self, request, *args, **kwargs):
        zonestr = kwargs['pk']
        if zonestr not in zone_account_dict:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        return Response(zone_account_dict[zonestr], status=status.HTTP_200_OK)


class ZoneScoreViewSet(mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    """获取各个类型的score信息"""
    queryset = set()

    def retrieve(self, request, *args, **kwargs):
        zonestr = kwargs['pk']
        if zonestr not in zone_score_dict:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        return Response(zone_score_dict[zonestr], status=status.HTTP_200_OK)


# 作废
class MoviePagination(PageNumberPagination):
    """电影分页"""
    page_size = 10  # 每页显示数据条数
    page_query_param = 'page'  # 哪一页
    page_size_query_param = 'page_size'  # 用于调整每页显示条数
    max_page_size = 20  # 最大的每页显示数据条数


# 作废
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


# 作废
class MovieGenresViewSet(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """电影流派枚举序列化"""
    serializer_class = MovieGenresSerializer
    queryset = MovieGenres.objects.all()
