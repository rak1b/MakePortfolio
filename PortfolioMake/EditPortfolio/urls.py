
from django.contrib import admin
from django.urls import path,include
from .views import editView, CreateheroView,getMyHero,ProjectView,showProjectView
urlpatterns = [
    path("",editView,name="edit"),
    path("hero/create/",CreateheroView,name="hero_create"),
    path("hero/get/",getMyHero,name="hero_get"),
    path("projects/add/",ProjectView.as_view(),name="add_projects"),
    # path("projects/show/",showProjectView.as_view(),name="show_projects"),

]
