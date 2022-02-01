from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# In order to create a view in Django, we're going to define a function.

def index(request): 
    return HttpResponse("Hello, world!");

def brian(request):
    return HttpResponse("Hello, Brian!");