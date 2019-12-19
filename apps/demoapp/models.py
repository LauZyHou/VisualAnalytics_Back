from datetime import datetime

from django.db import models


# Create your models here.

class Demo(models.Model):
    """测试用的demo类"""
    name = models.CharField(max_length=20, verbose_name="demo名字")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "demo"
        verbose_name_plural = "demos"

    def __str__(self):
        return self.name
