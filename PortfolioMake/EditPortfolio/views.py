import re
from django.http import JsonResponse,Http404
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from .models import *
from .forms import editorForm

from Portfolio_Theme.models import Theme
# Create your views here.


def editView(request):
    hero_contents = heroModel.objects.filter(username=request.user).first()
    hero_contents_default = heroModel.objects.filter(
        username="default").first()
    theme = Theme.objects.filter(user=request.user.id).first()

    form = editorForm

    # FOR PROJECT
    if request.user.is_authenticated:
        pmodel = projectsModel.objects.filter(user = request.user)
    else:
        pmodel = ''
            
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
        'projects' : pmodel,
        'theme':theme
    })


def getMyHero(request):
    data = heroModel.objects.filter(username=request.user.username).values()
    print("_______________________________")
    print(data)
    print("_______________________________")

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

    def get(self,request,id):
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
        id = request.POST['id']
        title = request.POST['title']
        image = request.FILES.get('image')
        short_description = request.POST['short_description']
        form = editorForm(request.POST)
        print("_____________________")
        print(id)
        print("_____________________")
        print(form)
        if form.is_valid():
            full_description = form.cleaned_data['full_description']
        # full_description = request.POST['short_description']
        else:
            full_description = ""
        print(full_description)
        user = request.user
        id=int(id)
        if id:
            pmodel = projectsModel.objects.filter(id=id).first()
            pmodel.title = title
            pmodel.short_description = short_description
            if image is not None:
                pmodel.image = image
            if full_description:
                pmodel.full_description = full_description
            pmodel.save()
            # update_pmodel = projectsModel(id=id,)
            print(title)
            print(image)
            
            print("full_description")
            print(full_description)
        else:
            psave = projectsModel.objects.create(
            user=user, title=title,image=image, short_description=short_description, full_description=full_description)
        return JsonResponse({
            'data': 'Project Added..',
            'status': 200
        })

    

class showProjectView(View):
    def post(self,request):
        print(request.POST['csrfmiddlewaretoken'])
        pmodel = projectsModel.objects.filter(id=request.POST['id']).values()
        print("_______________________________")
        print(pmodel)
        print("_______________________________")

        context ={
            'data' : list(pmodel)[0]
        }
        return JsonResponse(context)

class DeleteProjectView(View):
    def post(self,request,id):
        pmodel = projectsModel.objects.filter(id=id).first()
        pmodel.delete()
        # return HttpResponse('/')
        return redirect(request.META['HTTP_REFERER'])

    # def delete(self,request):
