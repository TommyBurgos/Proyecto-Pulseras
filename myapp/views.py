from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Paquete, Servicio

# Create your views here.
def index(request):
    title='AI.Tech - Artificial Intelligence HTML Template'
    return render(request, "index.html",{
        'title':title
    })
def hello(request,username):
    return HttpResponse("<h2>Hola %s</h2>"%username)

def about(request):
    return render(request,"about.html")

def paquetes(request):
    proyectos=list(Paquete.objects.values())
    return render(request, 'paquetes.html')

def servicios(request):
    #servicios= Servicio.objects.get(nombre=nombre)
    return render(request, 'servicios.html')

def registro(request):
    return render(request, 'registro.html')
