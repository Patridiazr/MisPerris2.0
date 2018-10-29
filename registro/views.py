from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect

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