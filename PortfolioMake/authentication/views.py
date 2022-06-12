from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.


def loginView(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Login done successfully")
    else:
        return HttpResponse("Email or Password Incorrect.")


def logout_view(request):
    logout(request)
    return redirect('/')


def signupView(request):
    if(request.method == "POST"):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username, email=email, password=password)
        print(user)
        print(username, email, password)

    return HttpResponse("Signup done")
