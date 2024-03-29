from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('paquetes/', views.paquetes),
    path('servicios/', views.servicios),
    path('registro/', views.registro),
    path('pagos/', views.pagos),
    path('login/', views.iniciar),
    path('contact/', views.contact),
    path('recuperacion/', views.recuperacion),
    path('detallePaquete/', views.detallePaquete),
    path('blogs/', views.blogs),
    path('crearPaquete/usAdmin', views.crearPaquete),
    path('login/usAdmin/',views.loginAdmin),
    path('detallePaqAdmin/usAdmin', views.detallePaqAdmin),
    path('dispositivosAdmin/usAdmin', views.dispositivosAdmin),
    path('ofertas/usAdmin', views.ofertas),
    path('paqueteAdmin/usAdmin', views.paqueteAdmin),
    path('crearCercos/', views.crearCercos),
    path('regitroExitoso/', views.registroExitoso, name='registroExitoso'),
    path('logout/', views.signout),
    path('infoCuenta/gestion', views.infoCuenta),
    path('configuracion/gestion', views.configuracion),
    path('metodos/gestion', views.metodos),
    path('transacciones/gestion', views.transacciones)
]