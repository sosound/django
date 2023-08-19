from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello World!')


def user_list(request):
    return HttpResponse('user list')


def user_add(request):
    return HttpResponse('user add')
