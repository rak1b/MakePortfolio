
from django.contrib import admin
from django.urls import path,include
from .views import editView, CreateheroView,getMyHero,addProjectView
urlpatterns = [
    path("",editView,name="edit"),
    path("hero/create/",CreateheroView,name="hero_create"),
    path("hero/get/",getMyHero,name="hero_get"),
    path("projects/add/",addProjectView,name="add_projects"),

]
