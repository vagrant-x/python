"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, re_path, include
from . import views, testdb, search, search2

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("runoob/", views.runoob),
    # path("testdb/", testdb.testdb)
    url(r'^hello/$', views.hello),
    url(r'^testdb/$', testdb.testdb),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', search2.search_post),

    # 路由
    # re_path("^index/([0-9]{4})/$", views.index),
    # re_path("^index/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.index2),
    url(r"^app01/", include('app01.urls')),  # 配置app01的路由

    # 反向解析
    # path("login/", views.login, name='login')
    # re_path(r"^login/([0-9]{2})/$", views.login, name='login')
    # re_path(r"^login/(?P<year>[0-9]{4})/$", views.login, name='login')

    # 命名空间
    path("login/", views.login, name='login'),
    path("app01/", include(("app01.urls", "app01")))
]

# from django.conf.urls import url
# from . import views
#
# urlpatterns = [
#     url(r'^$', views.hello)
# ]
