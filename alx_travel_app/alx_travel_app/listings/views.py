from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1> Index page </h1>")

def listings(response):
    return HttpResponse("<h1> listings page </h1>")