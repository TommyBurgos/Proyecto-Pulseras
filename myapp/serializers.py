from rest_framework import serializers 
from .models import DetalleServicio, PacienteDetalleServicio


class DetalleServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleServicio
        fields = '__all__'


class PacienteDetalleServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacienteDetalleServicio
        fields = '__all__'