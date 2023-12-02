from django.db import models

# Create your models here.

class Usuario ( models.Model):
    TipoUsuarios = [
        (0, 'Persona sin Auto'),#0-Persona sin auto
        (1, 'Conductor'),#1-COnductor
    ]
    user = models.CharField(max_length=30)
    mail = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    tipo_user = models.IntegerField(choices=TipoUsuarios)

    def __str__(self):
        return self.user


class Viaje (models.Model):
    patente = models.CharField(max_length=6,primary_key=True)
    duenno = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    salida = models.CharField(max_length=15)
    capacidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self) :
        return self.patente

