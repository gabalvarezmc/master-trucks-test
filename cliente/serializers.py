from rest_framework import serializers

from .models import  Cliente, Faena, Operacion


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'


class FaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faena
        fields = '__all__'


class OperacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operacion
        fields = '__all__'
