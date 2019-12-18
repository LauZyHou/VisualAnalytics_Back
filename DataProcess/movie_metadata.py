import pandas as pd
from typing import Dict, Set, List

"""
生成电影的元信息
"""


def meta1():
    """
    movie,title,平均rating,genres,imdbId,tmdId
    """
    links: pd.DataFrame = pd.read_csv('../DataSet/links.csv')
    movies: pd.DataFrame = pd.read_csv('../DataSet/movies.csv')
    ratings: pd.DataFrame = pd.read_csv('../DataSet/ratings.csv')
    tags: pd.read_csv = pd.read_csv('../DataSet/tags.csv')
    

if __name__ == '__main__':
    pass
