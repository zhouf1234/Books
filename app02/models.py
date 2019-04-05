from django.db import models

# Create your models here.

#验证F查询
class Goods(models.Model):
    # 商品名
    name=models.CharField(max_length=16)
    #收藏数
    keep_num=models.IntegerField()
    #购买数
    buy_num=models.IntegerField()


    def __str__(self):
        return self.name
