from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Usuario, Perro

#import de api
from rest_framework import viewsets
from .serializer import UsuarioSerializer, PerroSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def quienes(request):
    return render(request, 'quienes.html', {})


def contactenos(request):
    return render(request, 'contactenos.html', {})

def servicios(request):
    return render(request, 'servicios.html', {})

def adoptar(request):
    return render(request, 'adoptar.html', {})   

def login(request):
    return render(request, 'login.html',{})

def eliminar(request):
    return render(request, 'eliminar.html', {})

def listado(request):
    perro = Perro.objects.all()
    contexto = {'Disponibles': perro}
    return render (request, 'listado.html', contexto)   

def listado2(request):
    perro = Perro.objects.all()
    contexto = {'Disponibles': perro}
    return render (request, 'servicios.html', contexto)

#Crear Usuarios
def u_crear(request):
    rut = request.POST.get('rut', '')
    correo = request.POST.get('Email', '')
    nombre = request.POST.get('name', '')
    username = request.POST.get('username')
    fechanac = request.POST.get('fecha', '')
    telefono = request.POST.get('telefono', '')
    region = request.POST.get('region', '')
    ciudad = request.POST.get('comuna', '')
    tipoviv = request.POST.get('vivienda', '')
    contra = request.POST.get('con1','')
    usuario = Usuario(rut=rut, correo=correo, nombre=nombre, fechanac=fechanac,
                      telefono=telefono, region=region, ciudad=ciudad, tipoviv=tipoviv)
    usuario.save()
    user = User.objects.create_user(username=username, email=correo, password=contra)
    user.save()
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
    return redirect('adoptar')

def p_eliminar(request, id_p):
    perro = Perro.objects.get(id=id_p)
    perro.delete()
    return redirect('Listado')

def p_editar(request, id_p):
    perro = Perro.objects.get(pk=id_p)
    return render(request, 'editar.html', {'perro':perro})

def p_editado(request, id_p):
    p = Perro.objects.get(pk=id_p)
    foto = request.POST.get('foto', '')
    nombre = request.POST.get('nombre', '')
    raza = request.POST.get('raza', '')
    descripcion = request.POST.get('descripcion', '')
    estado = request.POST.get('estado', '')
    p.foto = foto
    p.nombre = nombre
    p.raza = raza
    p.descripcion = descripcion
    p.estado = estado
    p.save()
    return redirect('Listado')

#LOGIN
def login_iniciar(request):
    username = request.POST.get('rut', '')
    password = request.POST.get('contrasenia', '')
    user = authenticate(request, username=username, password=password)
    print(username, password)
    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto.");'+
                            ' window.location.href="/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); ' +
                            'window.location.href="/login/";</script>')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/login/')
def cerrar_session(request):
    logout(request)
    return HttpResponse('<script>alert("Cierre de sesión correcto.");'+
                        ' window.location.href="/";</script>')               

#Serialyzer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PerroViewSet(viewsets.ModelViewSet):
    queryset = Perro.objects.all()
    serializer_class = PerroSerializer