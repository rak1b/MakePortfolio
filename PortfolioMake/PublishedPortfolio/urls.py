
from django.contrib import admin
from django.urls import path,include
from .views import publishedView
urlpatterns = [
    path("<str:name>",publishedView,name="published"),
    # path("projects/show/",showProjectView.as_view(),name="show_projects"),

]
