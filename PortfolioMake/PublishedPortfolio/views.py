from django.http import HttpResponse
from django.shortcuts import render

from EditPortfolio.models import heroModel,projectsModel
from EditPortfolio.forms import editorForm
from django.contrib.auth.models import User
from Portfolio_Theme.models import Theme
from EditPortfolio.models import NavbarModel
# Create your views here.

def publishedView(request,name):
  user = User.objects.filter(username=name).first()
  navdetails = NavbarModel.objects.filter(user=user.id).first()

  if user:
    hero_contents = heroModel.objects.filter(username=name).first()
    hero_contents_default = heroModel.objects.filter(username="default").first()
    pmodel = projectsModel.objects.filter(user = user)
    theme = Theme.objects.filter(user=user).first()

    
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
        'projects' : pmodel,
        'theme':theme,
        'navbar':navdetails
        # 'color':bg_color
        
    })
  else:
    return HttpResponse("User dont exists,please create a account")

  # return render(request,'published/index.html',context)
# def publishedView(request,name):
#   data = heroModel.objects.filter(username=name).first()
#   # data = heroModel.objects.filter(username=request.user.username).first()
#   print(data)
#   context ={
#     data:data,
#   }
#   return render(request,'published/index.html',context)