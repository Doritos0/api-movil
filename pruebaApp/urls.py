from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import lista_usuarios, detalle_usuarios, lista_viaje, detalle_viaje, viajeTomado, enviar_correo, detalle_viaje_tomado

urlpatterns=[
    path('lista_usuarios/', lista_usuarios, name="lista_usuarios"),
    path('detalle_usuarios/<id>', detalle_usuarios, name="detalle_usuarios"),
    path('lista_viaje/', lista_viaje, name="lista_viaje"),
    path('detalle_viaje/<id>', detalle_viaje, name="detalle_viaje"),
    path('viajeTomado', viajeTomado, name="viajeTomado"),
    path('detalle_viaje_tomado/<id>', detalle_viaje_tomado, name="detalle_viaje_tomado"),
    path('enviar_correo/', enviar_correo, name="enviar_correo"),
]