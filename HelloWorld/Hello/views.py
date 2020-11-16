#Django
from django.shortcuts import render
from django.http import HttpResponse


def homePageView(request):
    """Se encarga de mostrar la pagina inicial"""
    return HttpResponse('Hello, World!')