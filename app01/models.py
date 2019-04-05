from django.db import models

# Create your models here.

#出版社表，写了总共四个表，生成五个，有一个自动创建
class Publisher(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=128)
    phone = models.IntegerField()

#作者表
class Author(models.Model):
    name = models.CharField(max_length=32)
    #作者和作者详情表一对一关联，一对一，不可重复
    detall = models.OneToOneField(to='AuthorDetall',on_delete=models.CASCADE)
    #作者和书的关系：多对多，自动生成了一个表
    books = models.ManyToManyField(to='Book')


    def __str__(self):
        return self.name


#作者的详情表
class AuthorDetall(models.Model):
    city = models.CharField(max_length=32)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    phone = models.IntegerField()

#书的表
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5,decimal_places=2)#最多五位数，最后两位是小数点
    #auto_now_add ：每次填写时的时间  auto_now：每次修改时的更新时间
    publish_day = models.DateField(auto_now_add=True)
    #书和出版社是多对一的关系，通过外键方式关联，CASCADE做级联操作
    publisher = models.ForeignKey(to='Publisher',on_delete=models.CASCADE)
    memo = models.CharField(max_length=128,null=True)

    def __str__(self):
        return self.title