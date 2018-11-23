from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.index, name="index"), 
    path('quienes/', views.quienes, name="quienes"),
    path('contactenos/', views.contactenos, name="contactenos"),
    path('registro/crear', views.u_crear, name="crear"),
    path('adoptar/', views.adoptar, name="adoptar"),
    path('servicios/', views.listado2, name="servicios"),
    path('listado/', views.listado, name="listado"),
    path('listado/crearP', views.r_crear, name="crearr"),
    path('listado/eliminar/<int:id_p>', views.p_eliminar, name="eliminar"),
    path('listado/editar/<int:id_p>', views.p_editar, name="editar"),
    path('listado/editado/<int:id_p>', views.p_editado, name="editado"),
        
    path('login/', views.login, name="login"),
    path('login/iniciar', views.login_iniciar, name="iniciar"),
    url(r'^cerrarsesion$', views.cerrar_session, name="cerrar_session"),
    url(r'^cerrarsesion$', views.cerrar_session, name="cerrar_session"),
    
    
]


