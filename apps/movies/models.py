from datetime import datetime

from django.db import models


# Create your models here.

class Movie(models.Model):
    """电影数据"""
    id = models.IntegerField(primary_key=True, verbose_name="ID")
    title = models.CharField(max_length=50, verbose_name="标题", null=True, blank=True)
    genres = models.CharField(max_length=100, verbose_name="流派", null=True, blank=True)
    tag = models.CharField(max_length=100, verbose_name="标签", null=True, blank=True)
    mean_rate = models.FloatField(verbose_name="平均得分", null=True, blank=True)
    imdb_id = models.CharField(max_length=8, verbose_name="IMDB ID", null=True, blank=True)
    tmdb_id = models.CharField(max_length=8, verbose_name="TMDB ID", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "电影"
        verbose_name_plural = "电影"

    def __str__(self):
        return str(self.id) + self.title


class MovieGenres(models.Model):
    """电影的流派枚举"""
    genre = models.CharField(max_length=20, verbose_name="流派", unique=True, null=False, blank=False)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "电影流派"
        verbose_name_plural = "电影流派"

    def __str__(self):
        return str(self.genre)
