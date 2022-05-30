from urllib import request
from django.shortcuts import render

# Create your views here.

def myPortfolioView(request):
    return render(request,'index.html')
