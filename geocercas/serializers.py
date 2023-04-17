from rest_framework import serializers

from .models import PuntosGeocercas, Geocerca, TipoGeocerca
from cliente.models import Faena, ZonaServicio

##################### GEOCERCA ####################

class GeocercasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geocerca
        fields = '__all__'
        depth = 1


class GeocercaSerializerCreate(serializers.ModelSerializer):
    faena = serializers.CharField()
    tipo_geocerca = serializers.CharField()
    zona_servicio = serializers.CharField()
    class Meta:
        model = Geocerca
        fields = '__all__'
        depth = 1
    
    def create(self, validated_data):
        tag = validated_data.pop('faena')
        tag_instance, created = Faena.objects.get_or_create(id=tag)
        tag2 = validated_data.pop('tipo_geocerca')
        tag_instance2, created = TipoGeocerca.objects.get_or_create(id=tag)
        tag2 = validated_data.pop('zona_servicio')
        tag_instance3, created = ZonaServicio.objects.get_or_create(id=tag)
        article_instance = Geocerca.objects.create(**validated_data, faena=tag_instance, tipo_geocerca=tag_instance2, zona_servicio=tag_instance3)
        return article_instance


class GeocercaSerializerUpdate(serializers.ModelSerializer):
    faena = serializers.CharField()
    tipo_geocerca = serializers.CharField()
    zona_servicio = serializers.CharField()
    class Meta:
        model = Geocerca    
        fields = '__all__'
        depth = 1
    def update(self, instance, validated_data):
        tag = validated_data.pop('faena')
        tag_instance, created = Faena.objects.get_or_create(id=tag)
        tag2 = validated_data.pop('tipo_geocerca')
        tag_instance2, created = TipoGeocerca.objects.get_or_create(id=tag2)
        tag3 = validated_data.pop('zona_servicio')
        tag_instance3, created = ZonaServicio.objects.get_or_create(id=tag3)
        instance.faena = tag_instance
        instance.tipo_geocerca = tag_instance2
        instance.zona_servicio = tag_instance3
        instance.nombre_geocerca = validated_data.get('nombre_geocerca', instance.nombre_geocerca)
        instance.save()
        return instance
    

##################### PUNTOS GEOCERCA ####################

class GeoDataSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = PuntosGeocercas
        fields = '__all__'
        depth = 1

class GeoDataSerializerUpdate(serializers.ModelSerializer):
    geocerca = serializers.CharField()
    class Meta:
        model = PuntosGeocercas
        fields = '__all__'
        depth = 1
    def update(self, instance, validated_data):
        tag = validated_data.pop('geocerca')
        tag_instance, created = Geocerca.objects.get_or_create(id=tag)
        instance.geocerca = tag_instance
        instance.latitud = validated_data.get('latitud', instance.latitud)
        instance.longitud = validated_data.get('longitud', instance.longitud)
        instance.save()
        return instance
    


class GeoDataSerializerCreate(serializers.ModelSerializer):
    geocerca = serializers.CharField()
    class Meta:
        model = PuntosGeocercas
        fields = '__all__'
        depth = 1
    
    def create(self, validated_data):
        tag = validated_data.pop('geocerca')
        tag_instance, created = Geocerca.objects.get_or_create(id=tag)
        article_instance = PuntosGeocercas.objects.create(**validated_data, geocerca=tag_instance)
        return article_instance


class GeoDataSerializerList(serializers.ModelSerializer):
    nombre_faena = serializers.CharField(source='geocerca.faena.nombre_faena')
    tipo_geocerca = serializers.CharField(source='geocerca.tipo_geocerca')
    nombre_geocerca = serializers.CharField(source='geocerca.nombre_geocerca')
    id_geocerca = serializers.CharField(source='geocerca.id')
    id_faena= serializers.CharField(source='geocerca.faena.id')
    class Meta:
        model = PuntosGeocercas
        fields = [
            'id',
            'latitud',
            'longitud',
            'id_faena',
            'nombre_faena',
            'id_geocerca',
            'nombre_geocerca',
            'tipo_geocerca',
            ]


##################### TIPO GEOCERCA ####################

class GeoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoGeocerca
        fields = '__all__'
        depth = 1
