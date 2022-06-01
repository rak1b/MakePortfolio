
from django.contrib import admin
from django.urls import path,include
from .views import editView, updateheroView
urlpatterns = [
    path("",editView,name="edit"),
    path("hero/",updateheroView,name="update"),
]
