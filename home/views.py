from atexit import register
from http.client import HTTPResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, "home/index.html")
