from atexit import register
from http.client import HTTPResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, "home/index.html")

def gallery(request):
    return render(request, "home/gallery.html")

def prewedding(request):
    return render(request, "home/prewedding.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")
