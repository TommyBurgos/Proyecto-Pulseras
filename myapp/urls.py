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
    path('login/', views.login),
    path('contact/', views.contact),
    path('recuperacion/', views.recuperacion)

]