from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

# Create your views here.

def index(request):
    return render (request,'index.html',{})

def quienes(request):
    return render (request,'quienes.html',{})

def contactenos(request):
    return render (request,'contactenos.html',{})

def servicios(request):
    return render (request,'servicios.html',{})

#Crud Usuarios
def U_Crear(request):
    rut = request.POST.get('rut','')
    correo = request.POST.get('Email','')
    nombre = request.POST.get('name','')
    fechaNac = request.POST.get('fecha','')
    telefono = request.POST.get('telefono','')
    region = request.POST.get('region','')
    ciudad = request.POST.get('comuna','')
    tipoViv = request.POST.get('vivienda','')
    usuario = Usuario(rut=rut,correo=correo,nombre=nombre,fechaNac=fechaNac,telefono=telefono,region=region,ciudad=ciudad,tipoViv=tipoViv)
    usuario.save()
    return HttpResponse('rut : '+rut+" correo: "+correo+" nombre: "+nombre+" fecha nacimiento: "+fechaNac+" telefono: "+telefono+" region: "+region+" ciudad: "+ciudad+" tipo vivienda: "+tipoViv)

#Crud Rescatados
def R_crear(request):
    foto = request.POST.get('foto','')
    nombre = request.POST.get('nombre','')
    raza = request.POST.get('raza','')
    descripcion = request.POST.get('descripcion','')
    estado = request.POST.get('estado','')
    return HttpResponse('foto : '+foto+" nombre: "+nombre+" raza: "+raza+" descripcion: "+descripcion+" estado: "+estado)
