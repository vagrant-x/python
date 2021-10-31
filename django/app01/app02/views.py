from django.shortcuts import render, HttpResponse
from app02 import models as app02_models


# Create your views here.
# 一对多： 方式一
# def add_book(request):
#     print("=======================>")
#     # 获取出版社对象
#     pub_obj = app02_models.Publish.objects.filter(pk=1).first()
#     # 给书籍的 publish属性传传 出版社对象
#     book = app02_models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2020-10-10", publish=pub_obj)
#     print(book, type(book))
#     return HttpResponse("app02_test 添加")

# def add_book(request):
#     print("=======================>")
#     # 获取出版社对象
#     pub_obj = app02_models.Publish.objects.filter(pk=1).first()
#     # 获取出版社对象的 id
#     pk = pub_obj.pk
#     # 给书籍的 publish属性传传 出版社对象的 id
#     book = app02_models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2020-10-10", publish_id=pk)
#     print(book, type(book))
#     return HttpResponse("app02_test 添加")

# def add_book(request):
#     print("=======================>")
#     # 获取作者对象
#     chong =  app02_models.Author.objects.filter(name="令狐冲").first()
#     ying = app02_models.Author.objects.filter(name="任盈盈").first()
#     # 获取书籍对象
#     book = app02_models.Book.objects.filter(title="菜鸟教程").first()
#     # 给书籍对象的 author 属性用 add 方法传作者对象
#     book.authors.add(chong, ying)
#     return HttpResponse(book)


# def add_book(request):
#     print("=======================>")
#     # 获取作者对象
#     chong =  app02_models.Author.objects.filter(name="令狐冲").first()
#     # 获取书籍对象
#     book = app02_models.Book.objects.filter(title="菜鸟教程2").first()
#     # 给书籍对象的 author 属性用 add 方法传作者对象的 id
#     book.authors.add(chong.pk)
#     return HttpResponse(book)

# def add_book(reuqest):
#     book_obj = app02_models.Book.objects.get(id=1)
#     author_list = app02_models.Author.objects.filter(id__gte=2)
#     # 方法一： 传递对象
#     book_obj.authors.add(*author_list)
#     # 方法二：传递对象id
#     book_obj.authors.add(*[1, 2, 3])

# def add_book(reuqest):
#     author = app02_models.Author.objects.filter(pk=2).first()
#     book_obj = app02_models.Book.objects.get(pk=1)
#     # 小写表名_set
#     author.book_set.add(book_obj)
#     return HttpResponse("OK")


# def add_book(reuqest):
#     pub = app02_models.Publish.objects.filter(name="明教出版社").first()
#     author = app02_models.Author.objects.filter(name="任我行").first()
#     # 使用 create方法： 插件书，关联出版社和作者
#     book = author.book_set.create(title="吸星大法", price=300, pub_date="1999-9-9", publish=pub)
#     return HttpResponse(book)


# def add_book(reuqest):
#     book = app02_models.Book.objects.get(pk=1)
#     author = app02_models.Author.objects.get(pk=2)
#     author.book_set.remove(book)
#     return HttpResponse("ok")

# def add_book(reuqest):
#     book = app02_models.Book.objects.get(pk=3)
#     book.authors.clear()
#     return HttpResponse("ok")

# def add_book(reuqest):
#     book = app02_models.Book.objects.filter(pk=1).first()
#     city = book.publish.city
#     return HttpResponse(city)

# def add_book(reuqest):
#     pub = app02_models.Publish.objects.filter(name="华山出版社").first()
#     q_set = pub.book_set.all()  # 对象.小写类名_set.all()
#     for b in q_set:
#         print(b.title)
#     return HttpResponse("ok")


# def add_book(reuqest):
#     author = app02_models.Author.objects.get(pk=1)
#     tel = author.au_detail.tel
#     return HttpResponse(tel)

# def add_book(reuqest):
#     ad = app02_models.AuthorDetail.objects.get(pk=1)
#     name = ad.author.name
#     return HttpResponse(name)

# def add_book(request):
#     book = app02_models.Book.objects.filter(title="菜鸟教程1").first()
#     authors = book.authors.all()
#     # 作者表里没有作者电话，因此再次通过对象.属性(i.au_detail)跳转到关联的表（作者详情表）。
#     for a in authors:
#         print(a.name, a.au_detail.tel)
#     return HttpResponse("ok")

# def add_book(request):
#     author = app02_models.Author.objects.filter(pk=2).first()
#     books = author.book_set.all()
#     for b in books:
#         print(b.title)
#     return HttpResponse("ok")

# def add_book(request):
#     # publish__name  属性名称__跨表的属性名称
#     res = app02_models.Book.objects.filter(publish__name="华山出版社").values_list("title", "price")
#     return HttpResponse(res)


# def add_book(request):
#     # book_name  小写类名__跨表的属性名称
#     res = app02_models.Publish.objects.filter(name="华山出版社").values_list("book__title", "book__price")
#     return HttpResponse(res)


# ===================================== 聚合查询 =================================================

from django.db.models import Avg, Max, Min, Sum, Count

# # 计算所有图书的平均价格
# def add_book(request):
#     res = app02_models.Book.objects.aggregate(Avg('price'))
#     print(res)
#     return HttpResponse(str(res))
#
# # 计算所有图书的数量、最贵价格和最便宜价格
# def add_book(request):
#     res = app02_models.Book.objects.aggregate(c=Count("id"), max=Max("price"), min=Min("price"))
#     print(res)
#     return HttpResponse(str(res))


# annotate

# # 统计每一个出版社的最便宜的书的价格：
# def add_book(request):
#     res = app02_models.Publish.objects.values("name").annotate(in_price=Min("book__price"))
#     print(res)
#     return HttpResponse("OK")
#
# # 统计每一本书的作者个数
# def add_book(request):
#     res = app02_models.Book.objects.annotate(c=Count("authors__name")).values("title", "c")
#     print(res)
#     return HttpResponse("OK")
#
# # 统计每一本以"菜"开头的书籍的作者个数
# def add_book(request):
#     res = app02_models.Book.objects.filter(title__startswith="菜").annotate(c=Count("authors__name")).values("title", "c")
#     print(res)
#     return HttpResponse("OK")
#
#
# # 统计不止一个作者的图书名称
# def add_book(request):
#     res = app02_models.Book.objects.annotate(c=Count("authors__name")).filter(c__gt=1).values("title", "c")
#     print(res)
#     return HttpResponse("OK")


# F 查询

# # 查询工资大于年龄的人
# from django.db.models import F
# def add_book(request):
#     res = app02_models.Emp.objects.filter(salary__gt=F("age")).values("name", "salary", "age")
#     print(res)
#     return HttpResponse("OK")
#
# # 将每一本书的价格提高1元
# def add_book(request):
#     res = app02_models.Book.objects.update(price=F("price") + 1)
#     print(res)
#     return HttpResponse("OK")


# Q 查询
from django.db.models import Q
# 查询价格大于 300 或者名称以菜开头的书籍的名称和价格
def add_book(request):
    res = app02_models.Book.objects.filter(Q(price__gte=300)| Q(title__startswith="菜")).values("title", "price")
    print(res)
    return HttpResponse("OK")

#查询以"菜"结尾或者不是 2010 年 10 月份的书籍
def add_book(request):
    res = app02_models.Book.objects.filter(Q(title__endswith="菜") | ~Q(Q(pub_date__year=2010) & Q(pub_date__month=10)))
    print(res)
    return HttpResponse("OK")

# 查询出版日期是 2004 或者 1999 年，并且书名中包含有"菜"的书籍。
# Q 对象和关键字混合使用，Q 对象要在所有关键字的前面:
def add_book(request):
    res = app02_models.Book.objects.filter(Q(Q(pub_date__year=2004) | Q(pub_date__year=1999)), title__contains="菜")
    print(res)
    return HttpResponse("OK")