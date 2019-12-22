import os
import sys

from typing import Dict
import pickle

"""
将电影流派的各个枚举字符串取值持久化到数据库
"""

# 将当前文件所在目录设置到django环境下
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VisualAnalysis.settings")

# 初始化django环境
import django

django.setup()

# 导入django内部的model必须在初始化django之后,不能放在最上边
from movies.models import MovieGenres

if __name__ == '__main__':
    genres_set = set()
    with open("../Jupyter/movie.pkl", 'rb') as f:
        movies: Dict = pickle.load(f)
        for k in movies:
            if 'genres' in movies[k]:
                genres_str = movies[k]['genres']
                genres_list = genres_str.split('|')
                genres_set = genres_set | set(genres_list)
        # 写入数据库
        for g in genres_set:
            movie_genre = MovieGenres()
            movie_genre.genre = g[:20]
            movie_genre.save()
