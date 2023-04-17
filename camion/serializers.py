from rest_framework import serializers

from .models import Vehiculo, SistemaControl, ModeloVehiculo, MarcaVehiculo

class VehiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehiculo
        fields = '__all__'

class VehiculoLastSeenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehiculo
        fields = ['id_mac', 'last_seen', 'last_latitud', 'last_longitud']
        # lookup_field = 'id_mac'


class VehiculoSerializerCreate(serializers.ModelSerializer):
    sistema_control = serializers.CharField()
    modelo = serializers.CharField()
    marca = serializers.CharField()
    class Meta:
        model = Vehiculo
        fields = '__all__'
        depth = 1
    
    def create(self, validated_data):
        tag = validated_data.pop('sistema_control')
        tag_instance, created = SistemaControl.objects.get_or_create(id=tag)
        tag2 = validated_data.pop('modelo')
        tag_instance2, created = ModeloVehiculo.objects.get_or_create(id=tag)
        tag2 = validated_data.pop('marca')
        tag_instance3, created = MarcaVehiculo.objects.get_or_create(id=tag)
        article_instance = Vehiculo.objects.create(**validated_data, sistema_control=tag_instance, modelo=tag_instance2, marca=tag_instance3)
        return article_instance