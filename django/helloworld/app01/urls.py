from django.conf.urls import url, re_path
from django.urls import path
from . import views

urlpatterns = [
    url(r'^app001/', views.app01_home),
    path("login/", views.login, name="login")
]