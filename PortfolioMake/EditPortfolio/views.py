from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.

def editView(request):
    hero_contents = heroModel.objects.filter(username="default").first()

    return render(request,"edit/editpage.html",context={
        'data':hero_contents
    })

    # before_name:before_name,
    #   name:name,
    #   before_desc:before_desc,
    #   desc:desc,

def updateheroView(request):
    print("-----------------------------")

    print(request.POST)
    print("-----------------------------")

    return HttpResponse("updated")

