from django.shortcuts import render, HttpResponse
from app01 import models


# def add_book(request):
#     # 方式一：实例化后执行save方法
#     # book = models.Book(title="菜鸟教程", price="30", publish="菜鸟出版社", pub_date="2021-8-8")
#     # book.save()
#
#     # 方式二：通过ORM 提供的objects 提供的方法 create来实现
#     book = models.Book.objects.create(title="菜鸟教程2", price="40", publish="菜鸟出版社", pub_date="2021-9-9")
#     print(book, type(book))
#     return HttpResponse("数据添加成功")

# def add_book(request):
#     books = models.Book.objects.all()
#     print(books)
#     print(type(books))
#     for b in books:
#         print(b.title)
#     return HttpResponse("all 查询对象成功")


# def add_book(request):
#     books = models.Book.objects.filter(pk=1)
#     print(books)
#     print(type(books))
#     for b in books:
#         print(b.id)
#     return HttpResponse("filter 查询对象成功")


# def add_book(request):
#     books = models.Book.objects.exclude(pk=1)
#     print(books)
#     print(type(books))
#     for b in books:
#         print(b.id)
#     return HttpResponse("exclude 查询对象成功")

# def add_book(request):
#     books = models.Book.objects.get(pk=1)
#     # books = models.Book.objects.get(pk=5)  # 5 不存在
#     print(books)
#     print(type(books))
#     return HttpResponse("get 查询对象成功")

# def add_book(request):
#     books = models.Book.objects.order_by("-price")
#     print(books)
#     print(type(books))
#     for b in books:
#         print(b.price)
#     return HttpResponse("order_by 查询对象成功")


# def add_book(request):
#     books = models.Book.objects.order_by("-price").reverse()
#     print(books)
#     print(type(books))
#     for b in books:
#         print(b.price)
#     return HttpResponse("reverse 查询对象成功")

# def add_book(request):
#     books = models.Book.objects.all().count()
#     print(books)
#     print(type(books))
#     return HttpResponse("count 查询对象成功")

# def add_book(request):
#     books = models.Book.objects.first()
#     print("第一个数据：{}".format(books))
#     books = models.Book.objects.last()
#     print("最后一个数据：{}".format(books))
#     print(type(books))
#     return HttpResponse("first last 查询对象成功")

# def add_book(request):
#     books = models.Book.objects.exists()
#     print(books)
#     print(type(books))
#     return HttpResponse("exists 查询对象成功")

# def add_book(request):
#     books = models.Book.objects.values("pk", "price")
#     print(books)
#     print(type(books))
#     return HttpResponse("values 查询对象成功")

# def add_book(request):
#     books = models.Book.objects.values_list("pk", "price")
#     print(books)
#     print(type(books))
#     return HttpResponse("values_list 查询对象成功")

# def add_book(request):
#     # 查出一共有多少个出版社
#     books = models.Book.objects.values_list("publish").distinct()
#     print(books)
#     print(type(books))
#     return HttpResponse("distinct 查询对象成功")


# def add_book(request):
#     # 查出一共有多少个出版社
#     print("=====> __in 用于读取区间，= 号后面为列表")
#     books = models.Book.objects.filter(price__in=[30, 40])
#     print(books)
#     print("=====> __gt 大于号 ，= 号后面为数字")
#     books = models.Book.objects.filter(price__gt=49)
#     print(books)
#     print("=====> __gte 大于等于，= 号后面为数字")
#     books = models.Book.objects.filter(price__gte=50)
#     print(books)
#     print("=====> __lt 小于，=号后面为数字")
#     books = models.Book.objects.filter(price__lt=31)
#     print(books)
#     print("=====> __lte 小于等于，= 号后面为数字")
#     books = models.Book.objects.filter(price__lte=30)
#     print(books)
#     print("=====> __range 在 ... 之间，左闭右闭区间，= 号后面为两个元素的列表")
#     books = models.Book.objects.filter(price__range=[30, 40])
#     print(books)
#     print("=====> __contains 包含，= 号后面为字符串")
#     books = models.Book.objects.filter(publish__contains='3')
#     print(books)
#     print("=====> __icontains 不区分大小写的包含，= 号后面为字符串")
#     books = models.Book.objects.filter(publish__icontains='a')
#     print(books)
#     print("=====> __startswith 以指定字符开头，= 号后面为字符串")
#     books = models.Book.objects.filter(publish__startswith='a')
#     print(books)
#     print("=====> __endswith 以指定字符结尾，= 号后面为字符串")
#     books = models.Book.objects.filter(publish__endswith='3A')
#     print(books)
#     print("=====> __year 是 DateField 数据类型的年份，= 号后面为数字")
#     books = models.Book.objects.filter(pub_date__year=2021)
#     print(books)
#     print("=====> __month 是DateField 数据类型的月份，= 号后面为数字")
#     books = models.Book.objects.filter(pub_date__month=10)
#     print(books)
#     print("=====> __day 是DateField 数据类型的天数，= 号后面为数字")
#     books = models.Book.objects.filter(pub_date__day=9)
#     print(books)
#
#     print(type(books))
#     for b in books:
#         print(b.pub_date)
#     return HttpResponse("filter 双下划线模糊 查询对象成功")


# def add_book(request):
#     books = models.Book.objects.filter(pk=5).first().delete()
#     print(books)
#     print(type(books))
#     return HttpResponse("delete 删除对象成功")

# def add_book(request):
#     books = models.Book.objects.filter(pk__in=[3, 4]).delete()
#     print(books)
#     print(type(books))
#     return HttpResponse("delete 删除对象成功")

# def add_book(request):
#     books = models.Book.objects.filter(pk=3)[0]
#     books.title = "title3"
#     books.save()
#     print(books)
#     print(type(books))
#     return HttpResponse("update 修改对象成功")

def add_book(request):
    books = models.Book.objects.filter(pk=3).update(price=888)
    print(books)
    print(type(books))
    return HttpResponse("update 修改对象成功")
