from django.db import models

class Infos(models.Model):
    poster_id = models.IntegerField(null=False)  # 用户id
    info = models.TextField(null=False, default=None)  # 文本信息
    latitude = models.FloatField(null=False, default=0.00000)  # 纬度
    longitude = models.FloatField(null=False, default=0.00000)  # 经度
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
