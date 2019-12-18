import pandas as pd
from typing import List, Dict, Set

"""
生成genres子标签
"""

if __name__ == '__main__':
    # links: pd.DataFrame = pd.read_csv('../DataSet/links.csv')
    movies: pd.DataFrame = pd.read_csv('../DataSet/movies.csv')
    # ratings: pd.DataFrame = pd.read_csv('../DataSet/ratings.csv')
    # tags: pd.read_csv = pd.read_csv('../DataSet/tags.csv')

    genres: Set = set()
    for s in movies.loc[:, 'genres'].values:
        genre_list = s.split('|')
        genres |= set(genre_list)

    print(genres)

