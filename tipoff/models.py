from django.db import models

# Create your models here.
class Tipoff(models.Model):
    poster_id = models.IntegerField(null=False)  # 用户id
    info_id = models.IntegerField(null=False)  # 信息id
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间