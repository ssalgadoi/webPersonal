#En las vistas de cada aplicacion, 
#Aca aplicamos la logica de lo que hace la pagina web cuando interactua con las apps

from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "core/home.html")#Aca estamos definiendo la Vista

def about(request):
    return render(request, "core/about-me.html")

def contact(request):
    return render(request, "core/contact.html")