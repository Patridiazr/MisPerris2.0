from django.urls import path,include
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'perro', views.PerroViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('registro/templates/index.html', views.index, name="index"),
    path('registro/templates/quienes.html', views.quienes, name="quienes"),
    path('registro/templates/contactenos.html', views.contactenos, name="contactenos"),
    #path('registro/templates/servicios.html', views.servicios, name="servicios"),
    path('registro/crear', views.u_crear, name="crear"),
    path('registro/templates/adoptar.html', views.adoptar, name="adoptar"),
    path('registro/templates/login.html', views.login, name="login"),
    path('registro/templates/servicios.html', views.listado2, name="servicios"),
    path('registro/templates/listado.html', views.listado, name="Listado"),
    path('registro/crearP', views.r_crear, name="crearr"),
    path('registro/eliminar/<int:id_p>', views.p_eliminar, name="eliminar"),
    path('registro/editar/<int:id_p>', views.p_editar, name="editar"),
    path('registro/editado/<int:id_p>', views.p_editado, name="editado"),
    path('api/', include(router.urls)),
    
    url(r'^login/$', views.login, name="login"),
    url(r'^login/iniciar/$', views.login_iniciar, name="iniciar"),
    url(r'^cerrarsesion$', views.cerrar_session, name="cerrar_session"),
    url(r'^cerrarsesion$', views.cerrar_session, name="cerrar_session"),
    
    
]


