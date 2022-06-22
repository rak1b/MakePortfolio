from django.contrib import admin

# Register your models here.
from .models import Theme


class themeAdmin(admin.ModelAdmin):
    list_display = ("user", "color1","color2","color3",)

admin.site.register(Theme, themeAdmin)