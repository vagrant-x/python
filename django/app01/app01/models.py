from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)  # id 会自动创建，可以手动写入
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.CharField(max_length=32)
    pub_date = models.DateField()
