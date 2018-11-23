from rest_framework import serializers
from .models import Usuario, Perro


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('url','rut','correo','contrasenia','nombre','fechanac','telefono','region','ciudad','tipoviv') 

class PerroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perro
        fields = ('url','foto','nombre','raza','descripcion','estado') 