from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.

def editView(request):
    hero_contents = heroModel.objects.filter(username="default").first()
    print("-----------------------------")
    print(hero_contents)
    print(hero_contents.username)
    print("-----------------------------")

    return render(request,"edit/editpage.html",context={
        'data':hero_contents
    })

def updateheroView(request):
    print(request.data)
    return HttpResponse("updated")