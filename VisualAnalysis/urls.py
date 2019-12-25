"""VisualAnalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.static import serve
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from VisualAnalysis.settings import MEDIA_ROOT
from demoapp.views import DemoViewSet
from movies.views import MovieViewSet, MovieGenresViewSet
from movies.views import TypeViewSet, MeanScoreViewSet, \
    ScoreDistributionViewSet, MVAndPNumViewSet, ScoreFlowViewSet, \
    TypeDirectorViewSet, TypeScoreViewSet, TypeAccountViewSet, \
    ZoneViewSet, ZoneScoreViewSet, ZoneAccountViewSet, ZoneDirectorViewSet

# DRF:REST风格的router
router = DefaultRouter()
# router.register(r'demo', DemoViewSet, base_name='demo')
# router.register(r'movie', MovieViewSet, base_name='movie')
# router.register(r'movie_genres', MovieGenresViewSet, base_name='movie_genres')

# list电影的类型
router.register(r'type_list', TypeViewSet, base_name='type_list')
# list城市的类型
router.register(r'zone_list', ZoneViewSet, base_name='zone_list')
# list从1925到2016的平均得分(世界/中国大陆)
router.register(r'mean_score', MeanScoreViewSet, base_name='mean_score')
# list在[0, 5, 6.5, 7.5, 8, 8.5, 9, 10]两两区间下的score分布
router.register(r'score_distri', ScoreDistributionViewSet, base_name='score_distri')
# list电影数目、评论数目随时间的变化(1920-2016)
router.register(r'mvnum_pnum', MVAndPNumViewSet, base_name='mvnum_pnum')
# list从2010-2016年五个区间评分的电影数目变化
router.register(r'score_flow', ScoreFlowViewSet, base_name='score_flow')
# retrieve按类型名获取最常见的四个导演和score分布
router.register(r'type_director', TypeDirectorViewSet, base_name='type_director')
# retrieve按地区名获取最常见的四个导演和score分布
router.register(r'zone_director', ZoneDirectorViewSet, base_name='zone_director')
# retrieve按类型名获取score分布
router.register(r'type_score', TypeScoreViewSet, base_name='type_score')
# retrieve按类型名获取account分布
router.register(r'type_account', TypeAccountViewSet, base_name='type_account')
# retrieve按地区名获取score分布
router.register(r'zone_score', ZoneScoreViewSet, base_name='zone_score')
# retrieve按地区名获取account分布
router.register(r'zone_account', ZoneAccountViewSet, base_name='zone_account')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title="可视分析文档")),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找,使用配置好的路径
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
]
