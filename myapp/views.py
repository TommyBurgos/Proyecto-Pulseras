from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Paquete, Servicio, Dispositivo, BlogNoticia, Paciente, Medico, Alerta
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from user.models import User, Rol  # Importa tu nueva clase User personalizada
from .forms import UserForm
# New
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
import re




# from .forms import ChangePasswordForm

paquete1 = "Paquete Amigo (Básico)"
precio = 15
# nombresPaquetes=list([Paquete.objects.values.name])
# preciosPaquetes=list([Paquete.objects.values.precio])

# Create your views here


def index(request):
    title = 'AI.Tech - Pulseras Wifi'
    paquetes = Paquete.objects.all()
    blogs = BlogNoticia.objects.all()
    return render(request, "index.html", {
        'title': title,
        'paquetes': paquetes,
        'blogs': blogs
    })


def hello(request, username):
    return HttpResponse("<h2>Hola %s</h2>" % username)


def about(request):
    return render(request, "about.html")


def catalogDispositivo(request):
    dispositivos = Dispositivo.objects.all()
    return render(request, 'catalogDispositivo.html', {'dispositivos': dispositivos})


def detalleDispositivo(request, id):
    dispositivo = get_object_or_404(Dispositivo, id=id)
    return render(request, 'detalleDispositivo.html', {'dispositivo': dispositivo})


def pagoDispositivo(request, id):
    dispositivo = get_object_or_404(Dispositivo, id=id)
    return render(request, 'pagoDispositivo.html', {'dispositivo': dispositivo})


def historialRutas(request):
    return render(request, 'historialRutas.html')


def notificaciones(request):
    return render(request, 'notificaciones.html')


def servicios(request):
    dispositivos = Dispositivo.objects.all()
    paquetes = Paquete.objects.all()
    return render(request, 'servicios.html', {
        'dispositivos': dispositivos,
        'paquetes': paquetes,
    })


def registro(request):
    return render(request, 'registro.html', {'form': UserCreationForm})


def pagosX(request):
    return render(request, 'pagos.html', {
        'paquete1': paquete1,
        'precio': precio})


def iniciar(request):
    return render(request, 'login.html')


def contact(request):
    return render(request, 'contact.html')


def recuperacion(request):
    return render(request, 'recuperacion.html')


def detallePaquete(request, id):
    paquete = get_object_or_404(Paquete, id=id)
    return render(request, 'detallePaquete.html', {'paquete': paquete})


def pagos(request, id):
    paquete = get_object_or_404(Paquete, id=id)
    return render(request, 'pagos.html', {'paquete': paquete})


def blogs(request):
    blogs= BlogNoticia.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})


def detalleBlogs(request, id):
    blog = get_object_or_404(BlogNoticia, id=id)
    return render(request, 'detalleBlogs.html', {'blog': blog})


def crearCercos(request):
    return render(request, 'crearCercos.html')


def blogUser(request):
    return render(request, 'usGeneral/blog.html')


# Paginas de Gestion de cuenta
@login_required
def infoCuenta(request):
    return render(request, 'gestion/infoCuenta.html')


@login_required
def configuracion(request):
    return render(request, 'gestion/configuracion.html')


@login_required
def metodos(request):
    return render(request, 'gestion/metodos.html')


@login_required
def transacciones(request):
    return render(request, 'gestion/transacciones.html')


# GENERAL
# @login_required
def inicioGeneral(request):
    return render(request, 'usGeneral/index.html')


# PACIENTE
# @login_required
def inicioPaciente(request):
    return render(request, 'usPaciente/index.html')


# FAMILIAR
# @login_required
def inicioFamiliar(request):
    return render(request, 'usFamiliar/index.html')


# DOCTOR
# @login_required
def inicioDoctor(request):
    return render(request, 'usDoctor/panelDoctor.html')


def aggcita(request):
    return render(request, 'usDoctor/citas.html')


def aggreceta(request):
    return render(request, 'usDoctor/recetaMedica.html')


def dirigirPorRol(request, user):
    rol = user.rol_id
    if rol == 1:
        login(request, user)
        return render(request, 'usAdmin/index.html', {
            'usuario': user.first_name
                })
    if rol == 2:
        login(request, user)
        return render(request, 'usDoctor/panelDoctor.html', {
                    'usuario': user.first_name
                })
    if rol == 3:
        login(request, user)
        return render(request, 'usFamiliar/index.html', {
                    'usuario': user.first_name
                })


# Páginas Administrador
# @login_required
def loginAdmin(request):
    print("HE INGRESADO A LA SESION pero no entro al if")
    if request.method == 'GET':
        # user = authenticate(request, username=request.POST['idNumber'], password= request.POST['password'])
        return render(request, 'usAdmin/index.html')

    else:
        # return render(request, 'usAdmin/index.html')
        print("usuario intento")
        print(request.POST)
        user = authenticate(request, username=request.POST['idNumber'], password=request.POST['password'])
        print("usuario "+request.POST['idNumber'])

        print("HE INGRESADO A LA SESION")
        if user is None:
            return render(request, 'login.html', {
                'error': 'Username o password son incorrectas'
            })
        else:
            return dirigirPorRol(request, user)


@login_required
def crearPaquete(request):
    return render(request, 'usAdmin/crearPaquete.html')


@login_required
def detallePaqAdmin(request):
    return render(request, 'usAdmin/detallePaqAdmin.html')


@login_required
def dispositivosAdmin(request):
        dispositivos = Dispositivo.objects.all()
        busqueda = request.GET.get("buscar")
        if busqueda:
            dispositivos = Dispositivo.objects.filter(Q(serie=busqueda)).distinct()
            print("entre al if de busqueda")
        return render(request, 'usAdmin/dispositivosAdmin.html', {'dispositivos': dispositivos})


@login_required
def revisionPlanes(request):
    return render(request, 'usAdmin/revisionPlanes.html')


def solicitudCompra(request):
    return render(request, 'usAdmin/solicitudCompra.html')


def ofertas(request):
    return render(request, 'usAdmin/ofertas.html')


@login_required
def paqueteAdmin(request):
    return render(request, 'usAdmin/paqueteAdmin.html')


def registroExitoso(request):
    print(request.POST)
    print(request.POST['password'] == request.POST['confirmPassword'])
    print('ps1 ->'+request.POST['password'])
    print('ps2 ->'+request.POST['confirmPassword'])
    print('usuario //'+ request.POST['idNumber'])
    if request.POST['password'] == request.POST['confirmPassword']:
        try:
            password = request.POST.get('password')
            confirmPassword = request.POST.get('confirmPassword')
            idNumber = request.POST.get('idNumber')
            email = request.POST.get('email')
            print("Apenas ingrese")

            # print(user.rol_id)
            idNumber = request.POST['idNumber']
            print(len(idNumber))
            print(len(password) < 8)
            print("Valor de verdad")
            print(re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password))
            if password != confirmPassword or len(password) < 8 or not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
                errorP = 'La contraseña debe tener al menos 8 caracteres y contener una combinación de letras y números'
                print(errorP)
            # Validar email
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                errorEmail = 'El formato del correo electrónico no es válido'

            # Validar idNumber
            if len(idNumber) != 10:
                errorCedula = 'El número de cédula debe tener exactamente 10 caracteres'
            if 'errorP' in locals() or 'errorEmail' in locals() or 'errorCedula' in locals():
                return render(request, 'registro.html', {
                    'errorP': errorP if 'errorP' in locals() else None,
                    'errorEmail': errorEmail if 'errorEmail' in locals() else None,
                    'errorCedula': errorCedula if 'errorCedula' in locals() else None,
                    'formData': {
                        'idNumber': idNumber,
                        'firstName': request.POST.get('firstName'),
                        'lastName': request.POST.get('lastName'),
                        'email': email,
                        'gender': request.POST.get('gender'),
                        'birthdate': request.POST.get('birthdate'),
                        'city': request.POST.get('city'),
                        'address': request.POST.get('address'),
                    }
                })
            user = User.objects.create_user(username=request.POST['idNumber'],
                                            password=request.POST['password'],
                                            first_name=request.POST['firstName'],
                                            last_name=request.POST['lastName'],
                                            email=request.POST['email'],
                                            genero_id=request.POST['gender'],
                                            nacimiento=request.POST['birthdate'],
                                            estadoCivil_id=1,
                                            ciudad=request.POST['city'],
                                            direccion=request.POST['address'],
                                            rol_id=3)
            print("Casi guardo")
            user.save()
            print("Guarde el usuario")
            paciente = Paciente.objects.create(estado_id=1, idDispositivo_id=1, idUsuario_id=user.id)
            print("Cree el paciente")
            paciente.save()
            login(request, user)
            print("Se guardo correctamente")
            print(user.rol_id)
            return dirigirPorRol(request, user)
        except:
            print("no se pudo")
            return HttpResponse('Usuario ya existe')
    return HttpResponse('Contraseñas no coinciden')


def detalleUsuarios(request):
    busqueda = request.GET.get("buscar")
    usuarios = User.objects.all().order_by('-date_joined')
    if busqueda:
        usuarios = User.objects.filter(Q(username=busqueda)
                                       | Q(first_name=busqueda)
                                       | Q(last_name=busqueda)
                                       | Q(email=busqueda)
                                       | Q(ciudad=busqueda)).distinct()
        print("entre al if de busqueda")
    print("LISTADO DE USUARIOS")
    print(usuarios)
    if request.method == 'POST':
        try:
            script_js = f"""
            alert("Usuario Creado correctamente")
            """
            context = {'script_js': script_js}
            print("Apenas ingrese")
            user = User.objects.create_user(username=request.POST['idNumber'],
                                            password=request.POST['password'],
                                            first_name=request.POST['firstName'],
                                            last_name=request.POST['lastName'],
                                            email=request.POST['email'],
                                            genero_id=request.POST['gender'],
                                            nacimiento=request.POST['birthdate'],
                                            estadoCivil_id=1,
                                            ciudad=request.POST['city'],
                                            direccion=request.POST['address'],
                                            rol_id=request.POST['userRole'])
            print("Casi guardo")
            user.save()
            # doctor=Medico.objects.create(estado_id=1, idDispositivo_id=1,idUsuario_id=user.id)
            # doctor.save()
            print("Se guardo correctamente")
            print(user.rol_id)
            return render(request, 'usAdmin/detalleUsuarios.html', {'context': context, 'usuarios': usuarios})
        except:
            print("no se pudo")
            return HttpResponse('Usuario ya existe')
    return render(request, 'usAdmin/detalleUsuarios.html', {'usuarios': usuarios})


@login_required
def registrarDispositivo(request):
    print(request.POST['numSerie'])
    try:
        print("Apenas ingrese")
        opcion = request.POST.get('opEstado')
        print(opcion)
        opcion2 = request.POST.get('opTipo')
        print(opcion2)
        dispositivo = Dispositivo.objects.create(serie=request.POST['numSerie'], estadoD_id=request.POST['opEstado'], tipo_id=request.POST['opTipo'])
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
    return render(request, 'login.html')


@login_required
def cambiarContrasena(request):
    user = request.user
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
                    return render(request, 'gestion/cambioContrasena.html')  # Redirige a la página de perfil o donde sea apropiado
                else:
                    messages.error(request, 'Las contraseñas nuevas no coinciden.')
            else:
                messages.error(request, 'La contraseña actual no es válida.')
    else:
        print("Me meti pa ACAAAAA")
        form = UserForm()

    return render(request, 'gestion/cambioContrasena.html', {
        'form': form
    })


def paquetes(request):
    paquetes = Paquete.objects.all()
    return render(request, 'paquetes.html', {'paquetes': paquetes})


def mostrar_alertas(request):
    alertas = Alerta.objects.filter(paciente=request.user, activa=True)
    return render(request, 'alertas.html', {'alertas': alertas})


def manejar_mediciones_paciente(request):
    # Lógica para obtener las mediciones del paciente
    # Verificar si alguna medición supera los umbrales definidos
    if medicion_supera_umbral:
        # Crear una nueva alerta
        Alerta.objects.create(
            paciente=request.user,
            mensaje="¡Alerta! La medición del paciente ha superado el umbral."
        )
