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
from movies.views import MovieTypeViewSet, MeanScoreViewSet

# DRF:REST风格的router
router = DefaultRouter()
# router.register(r'demo', DemoViewSet, base_name='demo')
# router.register(r'movie', MovieViewSet, base_name='movie')
# router.register(r'movie_genres', MovieGenresViewSet, base_name='movie_genres')

# list电影的类型
router.register(r'type_set', MovieTypeViewSet, base_name='type_set')
# list从1925到2016的平均得分(世界/中国大陆)
router.register(r'mean_score', MeanScoreViewSet, base_name='mean_score')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title="可视分析文档")),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找,使用配置好的路径
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
]
