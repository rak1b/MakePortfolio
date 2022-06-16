import re
from django.http import JsonResponse,Http404
from django.shortcuts import render, HttpResponse
from django.views import View
from .models import *
from .forms import editorForm
# Create your views here.


def editView(request):
    hero_contents = heroModel.objects.filter(username=request.user).first()
    hero_contents_default = heroModel.objects.filter(
        username="default").first()
    form = editorForm

    # FOR PROJECT
    pmodel = projectsModel.objects.filter(user = request.user)
            
    if hero_contents is not None:
        data = {
            "check": 1,
            'before_name': hero_contents.before_name,
            'name': hero_contents.fullname,
            'before_description': hero_contents.before_description,
            'description': hero_contents.description,
        }
    else:
        data = {
            "check": 0,
            'before_name': hero_contents_default.before_name,
            'name': hero_contents_default.fullname,
            'before_description': hero_contents_default.before_description,
            'description': hero_contents_default.description,
        }

    return render(request, "edit/editpage.html", context={
        'data': data,
        'form':form,
        'projects' : pmodel
    })


def getMyHero(request):
    data = heroModel.objects.filter(username=request.user.username).values()
    print(data)
    return JsonResponse({
        'data': list(data)[0]
    })


def CreateheroView(request):
    print("-----------------------------")

    print(request.POST)
    print("-----------------------------")
    if(request.method == "POST"):
        before_name = request.POST['before_name']
        name = request.POST['name']

        before_desc = request.POST['before_desc']
        desc = request.POST['desc']
        check = request.POST['check']

        if(int(check) == 1):
            hero = heroModel.objects.filter(username=request.user).first()
            print(hero)

            user_hero = heroModel(id=hero.id, username=request.user.username, before_name=before_name,
                                  fullname=name, before_description=before_desc, description=desc)
            print("_______________")
            print("in check........")
            print(check)
            print(hero)
            print(hero)
            print(hero.id)
            # print(user_hero)
            print("_______________")
            user_hero.save()

        else:
            print("not 1")
            print(check)

            user_hero = heroModel.objects.create(
                username=request.user, before_name=before_name, fullname=name, before_description=before_desc, description=desc)
        if(user_hero):
            return JsonResponse({
                'data': 'created',
                'status': 1

            })
    return JsonResponse({
        'data': 'Not created',
                'status': 0

    })


class ProjectView(View):

    def get(self,request):
        pmodel = projectsModel.objects.filter(user = request.user)
        context ={
            'projects' : pmodel
        }
        print("__________")
        print(pmodel)
        print("__________")

        return JsonResponse({
        'data': context,
        'status': 400

    })
    def post(self,request):
        title = request.POST['title']
        image = request.FILES.get('image')
        short_description = request.POST['short_description']
        form = editorForm(request.POST)
        print(form)
        if form.is_valid():
            full_description = form.cleaned_data['full_description']
        # full_description = request.POST['short_description']
        else:
            full_description = ""
        print(full_description)
        user = request.user

        psave = projectsModel.objects.create(
            user=user, title=title,image=image, short_description=short_description, full_description=full_description)
        return JsonResponse({
            'data': 'Project Added..',
            'status': 200
        })

    

class showProjectView(View):
    def get(self,request):
        pmodel = projectsModel.objects.filter(user = request.user)
        context ={
            'projects' : pmodel
        }
        # return render(request,'pr')
