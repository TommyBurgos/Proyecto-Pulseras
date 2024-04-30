from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('paquetes/', views.paquetes),
    path('catalogDispositivo/', views.catalogDispositivo),
    path('detalleDispositivo/', views.detalleDispositivo),
    path('pagoDispositivo/', views.pagoDispositivo),
    path('historialRutas/', views.historialRutas),
    path('servicios/', views.servicios),
    path('registro/', views.registro),
    path('pagos/<int:id>', views.pagos),
    path('login/', views.iniciar),
    path('contact/', views.contact),
    path('recuperacion/', views.recuperacion),
    path('detallePaquete/<int:id>', views.detallePaquete),
    path('blogs/', views.blogs),
    path('blogs/detalleBlogs/<int:id>', views.detalleBlogs),
    path('crearPaquete/usAdmin', views.crearPaquete),
    path('login/usAdmin/',views.loginAdmin),
    path('detallePaqAdmin/usAdmin', views.detallePaqAdmin),
    path('dispositivosAdmin/usAdmin', views.dispositivosAdmin),
    path('revisionPlanes/usAdmin', views.revisionPlanes),
    path('solicitudCompra/usAdmin', views.solicitudCompra),
    path('ofertas/usAdmin', views.ofertas),
    path('paqueteAdmin/usAdmin', views.paqueteAdmin),
    path('crearCercos/', views.crearCercos),
    path('regitroExitoso/', views.registroExitoso, name='registroExitoso'),
    path('regitroDispositivo/', views.registrarDispositivo, name='registroDispositivo'),
    path('logout/', views.signout),
    path('infoCuenta/gestion', views.infoCuenta),
    path('configuracion/gestion', views.configuracion),
    path('metodos/gestion', views.metodos),
    path('transacciones/gestion', views.transacciones),
    path('user/doctor', views.inicioDoctor),
    path('user/paciente', views.inicioPaciente),
    path('user/familiar', views.inicioFamiliar),
    path('user/', views.inicioGeneral),
    path('user/blog', views.blogUser),
    path('user/doctor/cita', views.aggcita),
    path('user/doctor/receta', views.aggreceta),
    path('configuracion/cambiarContrasena', views.cambiarContrasena),
    path('login/usAdmin/detalleUsuarios', views.detalleUsuarios)

]