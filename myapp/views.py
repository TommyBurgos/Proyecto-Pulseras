from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Paquete, Servicio

# Create your views here.
def index(request):
    return HttpResponse("Pagina index")
def hello(request,username):
    return HttpResponse("<h2>Hola %s</h2>"%username)

def about(request):
    return HttpResponse("about")

def paquetes(request):
    proyectos=list(Paquete.objects.values())
    return JsonResponse(proyectos, safe=False)

def servicios(request,nombre):
    servicios= Servicio.objects.get(nombre=nombre)
    return HttpResponse('servicios: %s' %servicios.nombre)

