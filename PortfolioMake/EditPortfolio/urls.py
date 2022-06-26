
from django.contrib import admin
from django.urls import path,include
from .views import editView, CreateheroView,getMyHero,ProjectView,showProjectView,DeleteProjectView
urlpatterns = [
    path("",editView,name="edit"),
    path("hero/create/",CreateheroView,name="hero_create"),
    path("hero/get/",getMyHero,name="hero_get"),
    path("projects/add/",ProjectView.as_view(),name="add_projects"),
    path("projects/view/",showProjectView.as_view(),name="view_project"),
    path("projects/delete/<int:id>",DeleteProjectView.as_view(),name="delete_project"),
    path("navbar/edit",ProjectView.as_view(),name="navbar_edit"),
    # path("projects/show/",showProjectView.as_view(),name="show_projects"),

]
