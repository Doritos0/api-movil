from django.db import models

# Create your models here.

class Usuario ( models.Model):
    TipoUsuarios = [
        (0, 'Persona sin Auto'),#0-Persona sin auto
        (1, 'Conductor'),#1-COnductor
    ]
    user = models.CharField(max_length=30, primary_key=True)
    mail = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=30)
    tipo_user = models.IntegerField(choices=TipoUsuarios)

    def __str__(self):
        return self.user


class Viaje (models.Model):
    TipoViaje = [
        (0, 'Ida'),#0-Viaje de Ida
        (1, 'Vuelta'),#1-Viaje de Vuelta
    ]
    EstadoViaje = [
        (0, 'Viaje Oculto'),#0-Oculto
        (1, 'Viaje Visible'),#1-Visible
    ]
    patente = models.CharField(max_length=6,primary_key=True)
    duenno = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    salida = models.CharField(max_length=15)
    fecha = models.CharField(max_length=20)
    capacidad = models.IntegerField()
    precio = models.IntegerField()
    tipo_viaje = models.IntegerField(choices=TipoViaje)
    estado_viaje = models.IntegerField(choices=EstadoViaje)

    def __str__(self) :
        return self.patente

class ViajeTomado (models.Model):
    EstadoViajeTomado = [
        (0, 'Viaje Finalizado'),#0-Viaje Finalizado
        (1, 'Viaje en Curso'),#1-Viaje en Curso
    ]
    id_viaje = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    viaje = models.ForeignKey(Viaje, on_delete= models.CASCADE)
    estado = models.IntegerField(choices=EstadoViajeTomado)

    def __str__(self):
        datos = "Usuario: "+self.usuario.user+" Patente: "+self.viaje.patente
        return datos
