from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Paquete, Servicio,Dispositivo
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from user.models import User  # Importa tu nueva clase User personalizada
from .forms import UserForm
#New
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from .forms import ChangePasswordForm

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

def catalogDispositivo(request):
    return render(request, 'catalogDispositivo.html')

def detalleDispositivo(request):
    return render(request, 'detalleDispositivo.html')

def pagoDispositivo(request):
    return render(request, 'pagoDispositivo.html')

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

def blogUser(request):
    return render (request, 'usGeneral/blog.html')

#Paginas de Gestion de cuenta
@login_required
def infoCuenta(request):
    return render(request,'gestion/infoCuenta.html')
@login_required
def configuracion(request):
    return render(request,'gestion/configuracion.html')
@login_required
def metodos(request):
    return render(request,'gestion/metodos.html')
@login_required
def transacciones(request):
    return render(request,'gestion/transacciones.html')
#GENERAL
#@login_required
def inicioGeneral(request):
    return render(request,'usGeneral/index.html')
#PACIENTE
#@login_required
def inicioPaciente(request):
    return render(request,'usPaciente/index.html')
#FAMILIAR
#@login_required
def inicioFamiliar(request):
    return render(request,'usFamiliar/index.html')
#DOCTOR
#@login_required
def inicioDoctor(request):
    return render(request,'usDoctor/panelDoctor.html')

def aggcita(request):
    return render (request,'usDoctor/citas.html')

def aggreceta(request):
    return render (request,'usDoctor/recetaMedica.html')

#Páginas Administrador
#@login_required
def loginAdmin(request):
    print("HE INGRESADO A LA SESION pero no entro al if")
    if request.method == 'GET':
        #user = authenticate(request, username=request.POST['idNumber'], password= request.POST['password'])                
        return render(request, 'usAdmin/index.html')
        
    else:
        #return render(request, 'usAdmin/index.html')
        print("usuario intento")
        print(request.POST)
        user = authenticate(request, username=request.POST['idNumber'], password= request.POST['password'])
        print("usuario "+request.POST['idNumber'])          
        
        print("HE INGRESADO A LA SESION")  
        if user is None:
            return render(request, 'login.html', {
                'error': 'Username o password son incorrectas'
            })
        else:
            rol=user.rol_id
            if rol ==1:
                login(request, user)
                return render(request, 'usAdmin/index.html', {
                    'usuario':user.first_name
                })
            if rol==2:
                login(request, user)
                return render(request, 'usDoctor/panelDoctor.html', {
                    'usuario':user.first_name
                })

@login_required
def crearPaquete(request):
    return render(request,'usAdmin/crearPaquete.html')

@login_required
def detallePaqAdmin(request):
    return render(request,'usAdmin/detallePaqAdmin.html')

@login_required
def dispositivosAdmin(request):
    dispositivos= Dispositivo.objects.all()
    return render(request,'usAdmin/dispositivosAdmin.html', {'dispositivos': dispositivos})


@login_required

def revisionPlanes(request):
    return render(request,'usAdmin/revisionPlanes.html')

def ofertas(request):
    return render(request,'usAdmin/ofertas.html')

@login_required
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
            password=request.POST['password'],first_name=request.POST['firstName'], last_name=request.POST['lastName'], email=request.POST['email'],genero_id=request.POST['gender'],nacimiento=request.POST['birthdate'],estadoCivil_id=request.POST['maritalStatus'],ciudad=request.POST['city'],direccion=request.POST['address'],rol_id=request.POST['userRole'])            
            print("Casi guardo")
            user.save()
            login(request, user)
            print("Se guardo correctamente")
            print(user.rol_id)
            return render(request,'usAdmin/index.html',{
                'usuario':user.first_name
            })            
        except:
            print("no se pudo")
            return HttpResponse('Usuario ya existe')
    return HttpResponse('Contraseñas no coinciden')
@login_required
def registrarDispositivo(request):
    print(request.POST['numSerie'])        
    try:
        print("Apenas ingrese")
        opcion=request.POST.get('opEstado')
        print(opcion)
        opcion2=request.POST.get('opTipo')
        print(opcion2)
        dispositivo=Dispositivo.objects.create(serie=request.POST['numSerie'],estadoD_id=request.POST['opEstado'], tipo_id=request.POST['opTipo'])
        print(dispositivo)                
        print("Casi guardo")
        dispositivo.save        
        print("Se guardo correctamente")
        return HttpResponse('Registrado Correctamente')
    except:
        print("no se pudo")
        return HttpResponse('No se pudo guardar')
    
def signout(request):
    logout(request)
    return render(request,'login.html')
@login_required
def cambiarContrasena(request):
    user=request.user
    if request.method == 'POST':
        print("Me meti pa ACA 2")
        form = UserForm(request.POST)
        if form.is_valid():
            print("Me meti pa ACA 3")
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_new_password = form.cleaned_data['confirm_new_password']
            if user.check_password(old_password):
                print("Me meti pa ACA 4")
                if new_password == confirm_new_password:
                    print("Me meti pa ACA SIIUUUU")
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Contraseña cambiada con éxito.')
                    return render(request,'gestion/cambioContrasena.html')  # Redirige a la página de perfil o donde sea apropiado
                else:
                    messages.error(request, 'Las contraseñas nuevas no coinciden.')
            else:
                messages.error(request, 'La contraseña actual no es válida.')
    else:
        print("Me meti pa ACAAAAA")
        form = UserForm()
    
    return render(request,'gestion/cambioContrasena.html', {
        'form':form        
    })