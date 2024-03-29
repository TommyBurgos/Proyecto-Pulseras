from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Paquete, Servicio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
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
    return render(request, 'registro.html', {'form':UserCreationForm})

def pagos(request):
    return render(request,'pagos.html',{
        'paquete1':paquete1,
        'precio':precio})

def iniciar(request):
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')

def recuperacion(request):
    return render(request, 'recuperacion.html')

def detallePaquete(request):
    return render(request, 'detallePaquete.html')

def blogs(request):
    return render(request,'blogs.html')

def crearCercos(request):
    return render(request,'crearCercos.html')


#Paginas de Gestion de cuenta
def infoCuenta(request):
    return render(request,'gestion/infoCuenta.html')

def configuracion(request):
    return render(request,'gestion/configuracion.html')

def metodos(request):
    return render(request,'gestion/metodos.html')

def transacciones(request):
    return render(request,'gestion/transacciones.html')


#Páginas Administrador

def loginAdmin(request):
    #return render(request, 'usAdmin/index.html')
    print("usuario intento")
    print(request.POST)
    user = authenticate(request, username=request.POST['idNumber'], password= request.POST['password'])
    print("usuario "+request.POST['idNumber'])    
    if user is None:
        return render(request, 'login.html', {
            'error': 'Username o password son incorrectas'
        })
    else:
        login(request, user)
        return render(request, 'usAdmin/index.html', {
            'usuario':user.first_name
        })

def crearPaquete(request):
    return render(request,'usAdmin/crearPaquete.html')

def detallePaqAdmin(request):
    return render(request,'usAdmin/detallePaqAdmin.html')

def dispositivosAdmin(request):
    return render(request,'usAdmin/dispositivosAdmin.html')

def ofertas(request):
    return render(request,'usAdmin/ofertas.html')

def paqueteAdmin(request):
    return render(request,'usAdmin/paqueteAdmin.html')

def registroExitoso(request):
    print(request.POST)
    print(request.POST['password'] == request.POST['confirmPassword'])
    print('ps1 ->'+request.POST['password'])
    print('ps2 ->'+request.POST['confirmPassword'])
    print('usuario //'+ request.POST['idNumber'])
    if request.POST['password'] == request.POST['confirmPassword']:
        try:
            print("Apenas ingrese")
            user=User.objects.create_user(username=request.POST['idNumber'],
            password=request.POST['password'],first_name=request.POST['firstName'], last_name=request.POST['lastName'], email=request.POST['email'])            
            print("Casi guardo")
            user.save()
            login(request, user)
            print("Se guardo correctamente")
            return render(request,'usAdmin/index.html')            
        except:
            print("no se pudo")
            return HttpResponse('Usuario ya existe')
    return HttpResponse('Contraseñas no coinciden')

def signout(request):
    logout(request)
    return render(request,'login.html')
