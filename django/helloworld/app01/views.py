from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def app01_home(request):
    return HttpResponse("app01_home")


def login(request):
    return HttpResponse("app01.login ！")
