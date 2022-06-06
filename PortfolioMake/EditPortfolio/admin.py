from django.contrib import admin
from .models import *

class HeroAdmin(admin.ModelAdmin):
    list_display = ("username", "fullname","description")
admin.site.register(heroModel, HeroAdmin)
