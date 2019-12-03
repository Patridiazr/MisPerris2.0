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
    path('quienes/', views.quienes, name="quienes"),
    path('contactenos/', views.contactenos, name="contactenos"),
    path('contactenos/crear', views.u_crear, name="crear"),
    path('adoptar/', views.adoptar, name="adoptar"),
    path('servicios/', views.listado2, name="servicios"),
    path('listado/', views.listado, name="listado"),
    path('listado/crearP', views.r_crear, name="crearr"),
    path('listado/eliminar/<int:id_p>', views.p_eliminar, name="eliminar"),
    path('listado/editar/<int:id_p>', views.p_editar, name="editar"),
    path('listado/editado/<int:id_p>', views.p_editado, name="editado"),
    path('api/', include(router.urls)),        
    path('login/', views.login, name="login"),
    path('login/iniciar', views.login_iniciar, name="iniciar"),
    path('cerrarsesion', views.cerrar_session, name="cerrar_session"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', include('pwa.urls')),
   
    
    
]


