from dataclasses import fields
from decimal import Clamped
from rest_framework import serializers
from .models import Boleto, Ruta, HorarioXTrayecto, Usuario, Bus, Trayecto, Asiento


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__' 

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['placa'] = validated_data['placa'].upper()

        bus = super().create(validated_data)
    
        for i in range(10):
            Asiento(bus = bus, numeroAsiento = i+1).save()

        return bus 
    
    def update(self, instance, validated_data):
        validated_data['placa'] = validated_data['placa'].upper()
        return super().update(instance, validated_data)
    
class TrayectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trayecto
        fields = '__all__'

class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = '__all__'


class BoletoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Boleto
        fields = '__all__'

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields= '__all__'

    def create(self, validated_data):
        validated_data['terminal'] = validated_data['terminal'].upper()
        validated_data['ciudad'] = validated_data['ciudad'].upper()

        return super().create(validated_data)

class HorarioXTrayectoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = HorarioXTrayecto
        fields = '__all__'
