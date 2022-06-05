
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')


def Contacto(request):
    return render(request, 'core/contacto.html')
