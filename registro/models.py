from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.IntegerField()
    correo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fechaNac = models.DateField()
    telefono = models.IntegerField()
    region = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    tipoViv = models.CharField(max_length=100)
    

class Perro(models.Model):
    imagen = models.ImageField(upload_to='fotos/')
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

