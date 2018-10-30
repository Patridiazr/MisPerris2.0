from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fechanac = models.DateField()
    telefono = models.IntegerField()
    region = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    tipoviv = models.CharField(max_length=100)
    

class Perro(models.Model):
    foto = models.ImageField(upload_to='{% static /images %}')
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

