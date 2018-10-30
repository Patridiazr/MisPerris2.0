from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Usuario, Perro


# Create your views here.

def index(request):
    return render (request, 'index.html', {})

def quienes(request):
    return render (request, 'quienes.html', {})

def contactenos(request):
    return render (request, 'contactenos.html', {})

def servicios(request):
    return render (request, 'servicios.html', {})

def adoptar(request):
    return render  (request, 'adoptar.html', {})   

def login(request):
    return render(request, 'login.html',{})

#Crear Usuarios
def u_crear(request):
    rut = request.POST.get('rut', '')
    correo = request.POST.get('Email', '')
    nombre = request.POST.get('name', '')
    fechanac = request.POST.get('fecha', '')
    telefono = request.POST.get('telefono', '')
    region = request.POST.get('region', '')
    ciudad = request.POST.get('comuna', '')
    tipoviv = request.POST.get('vivienda', '')
    usuario = Usuario(rut=rut, correo=correo, nombre=nombre, fechanac=fechanac,
                      telefono=telefono, region=region, ciudad=ciudad, tipoviv=tipoviv)
    usuario.save()
    return redirect('contactenos')

#Crud Rescatados
def r_crear(request):
    foto = request.POST.get('foto', '')
    nombre = request.POST.get('nombre', '')
    raza = request.POST.get('raza', '')
    descripcion = request.POST.get('descripcion', '')
    estado = request.POST.get('estado', '')
    perro = Perro(foto=foto, nombre=nombre, raza=raza, descripcion=descripcion, estado=estado)
    perro.save()
    return HttpResponse('foto : '+foto+" nombre: "+nombre+" raza: "+raza+" descripcion: "+descripcion+" estado: "+estado)

def p_buscar(request, id):
    perro = Perro.objects.get(pk=id)
    return perro

def p_editar(request, nombre_p):   

    perro = Perro.objects.get(nombre=nombre_p) 
    foto = request.POST.get('foto', '')
    nombre = request.POST.get('nombre', '')
    raza = request.POST.get('raza', '')
    descripcion = request.POST.get('descripcion', '')
    estado = request.POST.get('estado', '')
    perro = Perro.objets.get(pk=id)
    return redirect('perros(?)')



def login_iniciar(request):
    usuario = request.POST.get('rut','')
    contrasenia = request.POST.get('contrasenia','')
    user = authenticate(request, username=usuario, password=contrasenia)

    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto.");'+
                            'window.location.href="/index/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente...");'
                            +' window.location.href="/login/";</script>')

@login_required(login_url='/login/')
def cerrar_session(request):
    logout(request)
    return HttpResponse('<script>alert("Cierre de sesión correcto."); window.location.href="/index/";</script>')               
