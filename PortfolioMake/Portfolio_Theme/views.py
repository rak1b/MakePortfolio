from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from Portfolio_Theme.models import Theme
# Create your views here.
class UpdateColorView(View):
    def post(self,request):
        color1 = request.POST['color1']
        color2 = request.POST['color2']
        color3 = request.POST['color3']
        response = {'data':"Error"}
        print("In post________________________")
        
        # if(Theme.objects.filter(user=request.user.id).exists()):
        try:
            theme = Theme.objects.filter(id=request.user.id).first()
            theme.color1 = color1
            theme.color2 = color2
            theme.color3 = color3
            theme.save()
            if(theme):
                response = {'data':"updated"}
        except:
            theme = Theme.objects.create(user=request.user,color1=color1,color2=color2,color3=color3)
            if(theme):
                response = {'data':"created"}
        # return HttpResponse('/')
        

        return JsonResponse({
            'data':response
        })
