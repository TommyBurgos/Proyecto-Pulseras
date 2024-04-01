from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class Rol(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)
class EstadoCivil(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)

class Genero(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)
class User(AbstractUser):
    picture=models.ImageField(default='perfilDefecto.jpg')    
    nacimiento = models.DateField(default=datetime.date.today)
    ciudad=models.CharField(max_length=100, blank=True)
    direccion=models.CharField(max_length=300, blank=True)
    rol=models.ForeignKey(Rol,on_delete=models.CASCADE,default=5)
    estadoCivil=models.ForeignKey(EstadoCivil,on_delete=models.CASCADE,blank=True, default=1)
    genero=models.ForeignKey(Genero,on_delete=models.CASCADE, blank=True,default=3)
    

# Create your models here.



