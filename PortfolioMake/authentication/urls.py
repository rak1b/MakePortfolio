
from atexit import register
from tokenize import single_quoted
from django.contrib import admin
from django.urls import path,include
from .views import loginView,logout_view,signupView
urlpatterns = [
    path("mylogin/",loginView,name="login"),
    path("logout/",logout_view,name="logout"),
    path("register/",signupView,name='register')
]
