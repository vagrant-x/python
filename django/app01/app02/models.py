from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    # 外键在一对多的多中设置，models.ForeignKey("关联类名", on_delete=models.CASCADE)
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()  # 数据类型是邮箱格式


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密")
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()
