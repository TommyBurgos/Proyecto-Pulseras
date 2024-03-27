from django.db import models
from django.contrib.auth.models import User

class Medicamento(models.Model):
    name= models.CharField(max_length=100)
    indicaciones= models.CharField(max_length=150)

class Departamento(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)


class Medico(models.Model):
    idUsuario=models.ForeignKey(User,on_delete=models.CASCADE)
    departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE)

class EstadoCita(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)

class Estado(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)
class TipoDispositivo(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)
class EstadoDispositivo(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)
class Dispositivo(models.Model):
    tipo=models.ForeignKey(TipoDispositivo,on_delete=models.CASCADE)
    estadoD=models.ForeignKey(EstadoDispositivo,on_delete=models.CASCADE)
    serie=models.CharField(max_length=50)
    
class Paciente(models.Model):
    idUsuario=models.ForeignKey(User,on_delete=models.CASCADE)
    idDispositivo=models.ForeignKey(Dispositivo,on_delete=models.CASCADE)
    estado=models.ForeignKey(Estado,on_delete=models.CASCADE)


class RecetaMedica(models.Model):
    fechaEmision=models.DateField()
    idPaciente=models.ForeignKey(Paciente,on_delete=models.CASCADE)
    idMedico=models.ForeignKey(Medico,on_delete=models.CASCADE)

class DetalleReceta(models.Model):
    idReceta=models.ForeignKey(RecetaMedica,on_delete=models.CASCADE)
    idMedicamento=models.ForeignKey(Medicamento,on_delete=models.CASCADE)
    dosis= models.CharField(max_length=100)

class CitaMedica(models.Model):
    idPaciente=models.ForeignKey(Paciente,on_delete=models.CASCADE)
    idMedico=models.ForeignKey(Medico,on_delete=models.CASCADE)
    fechaCita=models.DateTimeField(auto_now_add=True)
    motivo=models.CharField(max_length=250)

# Create your models here.
class Paquete(models.Model):
    name= models.CharField(max_length=200)
    descripcion=models.TextField(blank=True)
    valor=models.IntegerField(default=0)

    def __str__(self):
        return self.name
class Servicio(models.Model):
    nombre= models.CharField(max_length=200)
    descripcion=models.TextField(blank=True)
    paquete=models.ForeignKey(Paquete, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + '-'+ self.paquete.name

class detallePaquete(models.Model):
    idPaquete=models.ForeignKey(Paquete,on_delete=models.CASCADE,blank=True)
    idServicio=models.ForeignKey(Servicio,on_delete=models.CASCADE,blank=True)
    
    



