from django.contrib import admin
from .models import Paquete, Servicio, Dispositivo, TipoDispositivo, EstadoDispositivo,BlogNoticia, PaqueteImagen, PaqueteServicio
# Register your models here.
admin.site.register(Paquete)
admin.site.register(Servicio)
admin.site.register(Dispositivo)
admin.site.register(TipoDispositivo)
admin.site.register(EstadoDispositivo)
admin.site.register(BlogNoticia)
admin.site.register(PaqueteImagen)
admin.site.register(PaqueteServicio)