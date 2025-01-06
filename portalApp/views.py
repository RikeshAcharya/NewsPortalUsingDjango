from django.shortcuts import render
from .models import News,Category
# Create your views here.

def home(request):
    dist={
        'news':News.objects.all(),
        'category':Category.objects.all(),
        'name':'hello'
    }
    return render(request,'index.html',dist)

def about(request):
    return render(request,'about.html')