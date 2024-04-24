from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def kazeem(request):
    return HttpResponse("Hello Kazeem!")

def fortune(request):
    return HttpResponse("Hello Fortune!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })