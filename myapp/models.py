from django.db import models

# Create your models here.
class Paquete(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Servicio(models.Model):
    nombre= models.CharField(max_length=200)
    descripcion=models.TextField()
    paquete=models.ForeignKey(Paquete, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + '-'+ self.paquete.name

