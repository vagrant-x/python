from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST 请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
# 在猎豹浏览器报错：CSRF verification failed. Request aborted.
# 改用谷歌浏览器
