from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Enfermedades(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.CharField(max_length=150)

class Medicamento(models.Model):
    name= models.CharField(max_length=100)
    indicaciones= models.CharField(max_length=150)

class Departamento(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)


class Medico(models.Model):
    idUsuario=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE)

class Especialidad(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)

class MedicoEspecialidad(models.Model):
    idMedico=models.ForeignKey(Medico,on_delete=models.CASCADE)
    idEspecialidad=models.ForeignKey(Especialidad,on_delete=models.CASCADE)
    fecha=models.DateField()

class EstadoCita(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)

class Estado(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)
class TipoDispositivo(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class EstadoDispositivo(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    tipo=models.ForeignKey(TipoDispositivo,on_delete=models.CASCADE)
    estadoD=models.ForeignKey(EstadoDispositivo,on_delete=models.CASCADE)
    serie=models.CharField(max_length=50)
    modelo=models.CharField(max_length=200, default="Modelo por default")
    color=models.CharField(max_length=150, default="Negro")
    version=models.CharField(max_length=250, default="Version 1.0.0")
    imgD=models.ImageField(upload_to='dispositivo_images/', default='dispositivo1.jpg')

class Paciente(models.Model):
    idUsuario=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    idDispositivo=models.ForeignKey(Dispositivo,on_delete=models.CASCADE)
    estado=models.ForeignKey(Estado,on_delete=models.CASCADE)

class pacienteDispositivo(models.Model):
    idPaciente=models.ForeignKey(Paciente,on_delete=models.CASCADE,blank=True, null=True)
    idDispositivo=models.ForeignKey(Dispositivo,on_delete=models.CASCADE,blank=True, null=True)
    fechaRegistro=models.DateField()
    fechaModificacion=models.DateField()

class CercoVirtual(models.Model):
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)

class CercoPaciente(models.Model):
    idPaciente=models.ForeignKey(Paciente,on_delete=models.CASCADE,blank=True, null=True)
    idCerco=models.ForeignKey(CercoVirtual,on_delete=models.CASCADE,blank=True, null=True)
    fecha=models.DateField()

class RolFamiliar(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class AntecedentesQuirurgicos(models.Model):
    idPaciente=models.ForeignKey(Paciente,on_delete=models.CASCADE,blank=True, null=True)
    fecha=models.DateField()
    descripcion=models.CharField(max_length=200)

class Familiar(models.Model):
    idUsuario=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
    rolFamiliar=models.ForeignKey(RolFamiliar,on_delete=models.CASCADE,blank=True, null=True)

class FamiliarPaciente(models.Model):
    idFamiliar=models.ForeignKey(Familiar,on_delete=models.CASCADE,blank=True, null=True)
    idPaciente=models.ForeignKey(Paciente,on_delete=models.CASCADE,blank=True, null=True)


class RecetaMedica(models.Model):
    fechaEmision=models.DateField()
    idPaciente=models.ForeignKey(Paciente,on_delete=models.CASCADE)
    idMedico=models.ForeignKey(Medico,on_delete=models.CASCADE)
    receta=models.CharField(max_length=1000, default="Consulte con su médico")

class DetalleReceta(models.Model):
    idReceta=models.ForeignKey(RecetaMedica,on_delete=models.CASCADE)
    idMedicamento=models.ForeignKey(Medicamento,on_delete=models.CASCADE)
    dosis= models.CharField(max_length=100)

class CitaMedica(models.Model):
    idPaciente=models.ForeignKey(Paciente,on_delete=models.CASCADE)
    idMedico=models.ForeignKey(Medico,on_delete=models.CASCADE)
    fechaCita=models.DateTimeField(auto_now_add=True)
    horaCita=models.TimeField(blank=True)
    motivo=models.CharField(max_length=250)

class BlogNoticia(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='blog_images/', default='blog1.jpg')
    titulo=models.CharField(max_length=200)
    noticia=models.CharField(max_length=100000)

class CentroMedico(models.Model):
    nombre= models.CharField(max_length=100)
    direccion= models.CharField(max_length=150)
    medicos = models.ManyToManyField(Medico)#Para que la relacion sea muchos a uno
    blog = models.ManyToManyField(BlogNoticia)
#Puedo probar
# Crear un centro médico
#centro_medico = CentroMedico.objects.create(nombre="Hospital XYZ", direccion="123 Calle Principal")
# Crear algunos médicos
#medico1 = Medico.objects.create(nombre="Dr. Juan Pérez")
#medico2 = Medico.objects.create(nombre="Dra. María Gómez")
# Asociar los médicos al centro médico
#centro_medico.medicos.add(medico1, medico2)


# Create your models here.


# Create your models here.
class Paquete(models.Model):
    name= models.CharField(max_length=200)
    descripcion=models.TextField(blank=True)
    valor=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class DetalleServicio(models.Model):
    fecha=models.DateField()
    hora = models.TimeField()
    medicion=models.CharField(max_length=200)

class Servicio(models.Model):
    nombre= models.CharField(max_length=200)
    umbral=models.TextField(blank=True)
    detalleServicio=models.ForeignKey(DetalleServicio, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre + '-'+ self.detalleServicio.medicion


class detallePaquete(models.Model):
    idPaquete=models.ForeignKey(Paquete,on_delete=models.CASCADE,blank=True)
    idServicio=models.ForeignKey(Servicio,on_delete=models.CASCADE,blank=True)

class PacientePaquete(models.Model):
    idPaciente=models.ForeignKey(Paciente,on_delete=models.CASCADE,blank=True)
    idPaquete=models.ForeignKey(Paquete,on_delete=models.CASCADE,blank=True)
    idDispositivo=models.ForeignKey(Dispositivo,on_delete=models.CASCADE,blank=True)
    fechaInicio=models.DateField()
    fechaFin=models.DateField()
    precio=models.FloatField()
    estado=models.ForeignKey(Estado,on_delete=models.CASCADE,blank=True)

class tipoAlerta(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.CharField(max_length=200)

class Alerta(models.Model):
    idPaciente=models.ForeignKey(Paciente,on_delete=models.CASCADE,blank=True, null=True)
    nombre= models.CharField(max_length=100)
    mensaje= models.TextField(default="Default")
    tipoAlerta=models.ForeignKey(tipoAlerta,on_delete=models.CASCADE)
    fechaCreacion= models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.mensaje



