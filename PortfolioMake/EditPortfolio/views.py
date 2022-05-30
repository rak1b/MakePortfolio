from django.shortcuts import render

# Create your views here.

def editView(request):
    return render(request,"edit/editpage.html")