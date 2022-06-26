"""PortfolioMake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from froala_editor import views
from django.urls import path, include
urlpatterns = [
    path("admin/dashboard/", admin.site.urls),
    path("", include("Portfolio_Theme.urls")),
    path("", include("MyPortfolio.urls")),
    path("", include("PublishedPortfolio.urls")),
    path("", include("authentication.urls")),
    path("edit/my/", include("EditPortfolio.urls")),
    path("accounts/", include("allauth.urls")),
    path('froala_editor/',include('froala_editor.urls')),

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


# https://www.geeksforgeeks.org/python-uploading-images-in-django/