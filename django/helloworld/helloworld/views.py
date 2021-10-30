from django.http import HttpResponse
from django.shortcuts import render, redirect


def hello(request):
    return HttpResponse("hello world!")


def runoob(request):
    name = "赞同图标"
    context = {"name": name}
    context["hello"] = "hello world!!"
    return render(request, "runoob.html", context)


def runoob2(request):
    name = "赞同图标"
    return render(request, "runoob.html", {"name": name})


# 正则路径中的无名分组
def index(request, year):
    print("year = {}".format(year))
    return HttpResponse("year = " + str(year))


# 正则路径中的有名分组
def index2(request, year, month):
    return HttpResponse("'year': {0}, 'month': {1}".format(year, month))

from django.urls import reverse
# def login(request, year):
#     print("yaer = {}".format(str(year)))
#     if request.method == "GET":
#         print("调用 get")
#         # return HttpResponse("这是一个GET请求")
#         return render(request, "login.html", {})
#         # return render(request, "runoob.html", {"name": "NAME"})
#     else:
#         print("调用 post")
#         print(request)
#         username = request.POST.get("username")
#         pwd = request.POST.get("pwd")
#         if username == "admin" and pwd == "admin":
#             return HttpResponse("登录成功")
#         else:
#             # url1 = reverse('login')
#             # print("解析后url: {}".format(url1))
#             # return redirect(url1)
#             return redirect(reverse('login', kwargs={"year": year}))


def login(request, year):
    print("yaer = {}".format(str(year)))
    if request.method == "GET":
        print("调用 get")
        return render(request, "login.html", {})
    else:
        print("调用 post")
        print(request)
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        if username == "admin" and pwd == "admin":
            return HttpResponse("登录成功")
        else:
            return redirect(reverse('login', kwargs={"year": year}))

def login(request):
    return redirect(reverse('app01:login'))




