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
    path('recuperacion/', views.recuperacion),
    path('detallePaquete/', views.detallePaquete),
    path('blogs/', views.blogs),
<<<<<<< HEAD
    path('crearPaquete/', views.crearPaquete)

=======
    path('login/usAdmin/',views.loginAdmin)
>>>>>>> f72f814b5eeff098b96767ca78f6df339accfb03

]