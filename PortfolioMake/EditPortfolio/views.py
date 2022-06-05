import re
from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.

def editView(request):
    hero_contents = heroModel.objects.filter(username=request.user).first()
    hero_contents_default = heroModel.objects.filter(username="default").first()

    if hero_contents is not None:
        data = {
            'before_name':hero_contents.before_name,
        'name':hero_contents.fullname,
        'before_description':hero_contents.before_description,
        'description':hero_contents.description,
        }
    else:
        data = {
        'before_name':hero_contents_default.before_name,
        'name':hero_contents_default.fullname,
        'before_description':hero_contents_default.before_description,
        'description':hero_contents_default.description,
        }

 

    return render(request,"edit/editpage.html",context={
        'data':data
    })

 

def updateheroView(request):
    print("-----------------------------")

    print(request.POST)
    print("-----------------------------")
    before_name = request.POST['before_name']
    name = request.POST['name']

    before_desc = request.POST['before_desc']
    desc = request.POST['desc']

    user_hero=heroModel.objects.create(username = request.user,before_name = before_name,fullname=name,before_description = before_desc,description = desc)


    return HttpResponse("updated")

