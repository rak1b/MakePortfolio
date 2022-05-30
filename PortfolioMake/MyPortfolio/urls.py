from django.urls import path
from .views import myPortfolioView
urlpatterns = [
    path("",myPortfolioView,name='my'),
]
