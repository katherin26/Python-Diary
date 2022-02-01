from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# In order to create a view in Django, we're going to define a function.

def index(request): 
    #return HttpResponse("Hello, world!")
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    #return HttpResponse(f"Hello, {name.capitalize()}")
    return render(request, "hello/greet.html",{
        "name" : name.capitalize()
    })