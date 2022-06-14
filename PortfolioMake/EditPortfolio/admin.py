from django.contrib import admin
from .models import *

class HeroAdmin(admin.ModelAdmin):
    list_display = ("username", "fullname","description")

class projectAdmin(admin.ModelAdmin):
    list_display = ("user", "title","short_description")

admin.site.register(heroModel, HeroAdmin)
admin.site.register(projectsModel, projectAdmin)
