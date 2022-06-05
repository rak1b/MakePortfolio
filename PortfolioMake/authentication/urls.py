
from django.contrib import admin
from django.urls import path,include
from .views import loginView,logout_view
urlpatterns = [
    path("mylogin/",loginView,name="login"),
    path("logout/",logout_view,name="logout"),
]
