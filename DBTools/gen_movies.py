import os
import sys

from typing import Dict
import pickle

"""
将电影数据持久化到数据库
"""

# 将当前文件所在目录设置到django环境下
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VisualAnalysis.settings")

# 初始化django环境
import django

django.setup()

# 导入django内部的model必须在初始化django之后,不能放在最上边
from movies.models import Movie

if __name__ == '__main__':
    # 读取文件,写入数据库
    with open("../Jupyter/movie.pkl", 'rb') as f:
        movies: Dict = pickle.load(f)
        cnt = 0
        for k in movies:
            print(movies[k])
            title = movies[k]['title'] if 'title' in movies[k] else None
            tag_list = movies[k]['tag'] if 'tag' in movies[k] else None
            genres = movies[k]['genres'] if 'genres' in movies[k] else None
            meanRating = movies[k]['meanRating'] if 'meanRating' in movies[k] else 0.0
            imdbId = str(movies[k]['imdbId']) if 'imdbId' in movies[k] else None
            tmdbId = str(movies[k]['tmdbId']) if 'tmdbId' in movies[k] else None

            tag = None if tag_list is None else '|'.join(tag_list)
            meanRating = None if meanRating is None else round(meanRating, 2)
            # print(title, tag, genres, meanRating, imdbId, tmdbId)
            # print(type(k), type(title), type(tag), type(genres), type(meanRating), type(imdbId), type(tmdbId))
            movie = Movie()
            movie.id = k
            movie.title = None if title is None else title[:50]
            movie.genres = None if genres is None else genres[:100]
            movie.tag = None if tag is None else tag[:100]
            movie.mean_rate = meanRating
            movie.imdb_id = None if imdbId is None else imdbId[:8]
            movie.tmdb_id = None if tmdbId is None else tmdbId[:8]

            movie.save()
