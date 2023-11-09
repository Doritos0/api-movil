from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import lista_usuarios, detalle_usuarios, lista_viaje, detalle_viaje

urlpatterns=[
    path('lista_usuarios/', lista_usuarios, name="lista_usuarios"),
    path('detalle_usuarios/<id>', detalle_usuarios, name="detalle_usuarios"),
    path('lista_viaje/', lista_viaje, name="lista_viaje"),
    path('detalle_viaje/<id>', detalle_viaje, name="detalle_viaje"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)