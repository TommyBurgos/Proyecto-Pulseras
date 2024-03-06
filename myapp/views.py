from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Paquete, Servicio
paquete1="Paquete Amigo (Básico)"
precio=15
#nombresPaquetes=list([Paquete.objects.values.name])
#preciosPaquetes=list([Paquete.objects.values.precio])
# Create your views here
def index(request):
    title='AI.Tech - Pulseras Wifi'    
    return render(request, "index.html",{
        'title':title,
        'paquete1':paquete1,
        'precio':precio

    })
def hello(request,username):
    return HttpResponse("<h2>Hola %s</h2>"%username)

def about(request):
    return render(request,"about.html")

def paquetes(request):
    #proyectos=list(Paquete.objects.values())
    return render(request, 'paquetes.html')

def servicios(request):
    #servicios= Servicio.objects.get(nombre=nombre)
    return render(request, 'servicios.html')

def registro(request):
    return render(request, 'registro.html')

def pagos(request):
    return render(request,'pagos.html',{
        'paquete1':paquete1,
        'precio':precio})

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')

def recuperacion(request):
    return render(request, 'recuperacion.html')

def blogs(request):
    return render(request,'blogs.html')