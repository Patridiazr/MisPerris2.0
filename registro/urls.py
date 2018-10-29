from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('',views.index,name="index"),
    path('registro/templates/index.html',views.index,name="index"),
    path('registro/templates/quienes.html',views.quienes,name="quienes"),
    path('registro/templates/contactenos.html',views.contactenos,name="contactenos"),
    path('registro/templates/servicios.html',views.servicios,name="servicios"),
    path('registro/crear',views.U_Crear,name = "crear")
]


