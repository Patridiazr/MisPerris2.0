from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render (request,'index.html',{})

def quienes(request):
    return render (request,'quienes.html',{})

def contactenos(request):
    return render (request,'contactenos.html',{})

def servicios(request):
    return render (request,'servicios.html',{})

def adoptar(request):
    return render  (request,'adoptar.html',{})   

def login(request):
    return render (request,'login.html',{})

#Crear Usuarios
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
    return redirect('contactenos')

#Crud Rescatados
def R_crear(request):
    foto = request.POST.get('foto','')
    nombre = request.POST.get('nombre','')
    raza = request.POST.get('raza','')
    descripcion = request.POST.get('descripcion','')
    estado = request.POST.get('estado','')
    return HttpResponse('foto : '+foto+" nombre: "+nombre+" raza: "+raza+" descripcion: "+descripcion+" estado: "+estado)
"""
def P_buscar(request,id):
    perro = Perro.objets.get(pk=id)
    return redirect('perros(?)')
"""

def login_iniciar(request):
    usuario = request.POST.get('rut','')
    contrasenia = request.POST.get('contrasenia','')
    user = authenticate(request,username=usuario, password=contrasenia)

    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto."); window.location.href="/index/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); window.location.href="/login/";</script>')

@login_required(login_url='/login/')
def cerrar_session(request):
    logout(request)
    return HttpResponse('<script>alert("Cierre de sesión correcto."); window.location.href="/index/";</script>')               