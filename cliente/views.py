from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.

from .models import (
    # Geocerca,
    # GeoData,
    Operacion,
    Faena,
    Cliente,

)

from .serializers import (

    ClienteSerializer,
    FaseSerializer,
    OperacionSerializer,
)


@api_view(['POST'])
def create_or_update_geodata(request):
    print(request.data)
    faena = request.data.get('faena')
    zona_de_servicio = request.data.get('zona_servicio')
    geocerca = request.data.get('geocerca')

    return Response(data={'asdf': 'asdfasdf'})


class OperacionView(generics.ListAPIView):

    def get_queryset(self):
        queryset = Operacion.objects.all()
        nombre_faena = self.request.query_params.get('nombre_faena')
        nombre_cliente = self.request.query_params('nombre_cliente')

        if nombre_faena:
            queryset = queryset.filter(faena__nombre_faena=nombre_faena)
        elif nombre_cliente:
            queryset = queryset.filter(faena__cliente__nombre_cliente=nombre_cliente)

        return queryset
