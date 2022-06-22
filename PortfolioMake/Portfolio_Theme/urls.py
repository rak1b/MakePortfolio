from django.urls import path
from .views import UpdateColorView
urlpatterns = [
    path('update_theme',UpdateColorView.as_view(),name="update_theme")
]
