from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return HttpResponse('<h1 style=\'color:blue\'>Hello, Sasa World</h1>')
def brian(request):
    return HttpResponse(' Sasa, Brian')
def david(request):
    return HttpResponse('Sasa, David')
def greet(request, name):
    return HttpResponse(f'<h1 style=\'color:blue\'>Sasa, {name.capitalize()}!</h1>')
