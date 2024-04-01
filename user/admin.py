from django.contrib import admin
from .models import User, Rol,EstadoCivil,Genero

admin.site.register(User)
admin.site.register(Rol)
admin.site.register(EstadoCivil)
admin.site.register(Genero)


# Register your models here.
