# from django.http import HttpResponse
from django.shortcuts import render
from math import ceil

# Create your views here.
def index(request):   
    return render(request, "index.html")