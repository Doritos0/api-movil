from rest_framework import serializers
from .models import Usuario, Viaje, ViajeTomado

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ViajeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = '__all__'

class ViajeTomadoSerializer (serializers.ModelSerializer):
    class Meta:
        model = ViajeTomado
        fields = '__all__'