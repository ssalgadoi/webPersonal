"""
URL configuration for webPersonal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from core import views as core_views#Importamos desde la app core todo lo que contiene views
from portfolio import views as portfolio_views

from django.conf import settings#Importamos el setting de nuestro proyecto

urlpatterns = [
    path('', core_views.home, name="home"),#Aca se hace referencia a las views donde va estar la url
    #por eso se deja vacio es la rais de lapgina web ,la portada
    path('about-me/', core_views.about, name="about"),
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),
    path('contact/', core_views.contact, name="contact"),
    path('admin/', admin.site.urls)
]

# Para ver las imagenes en el Admin
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)