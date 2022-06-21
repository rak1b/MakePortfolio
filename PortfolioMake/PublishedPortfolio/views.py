from django.http import HttpResponse
from django.shortcuts import render

from EditPortfolio.models import heroModel,projectsModel
from EditPortfolio.forms import editorForm
from django.contrib.auth.models import User

# Create your views here.

def publishedView(request,name):
    hero_contents = heroModel.objects.filter(username=name).first()
    # hero_contents = heroModel.objects.filter(username=request.user).first()
    hero_contents_default = heroModel.objects.filter(username="default").first()
    form = editorForm

    # FOR PROJECT
    if request.user.is_authenticated:
      pmodel = projectsModel.objects.filter(user = User.objects.get(username=name))
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

    return render(request, "published/index.html", context={
        'data': data,
        'form':form,
        'projects' : pmodel
    })

  # return render(request,'published/index.html',context)
# def publishedView(request,name):
#   data = heroModel.objects.filter(username=name).first()
#   # data = heroModel.objects.filter(username=request.user.username).first()
#   print(data)
#   context ={
#     data:data,
#   }
#   return render(request,'published/index.html',context)