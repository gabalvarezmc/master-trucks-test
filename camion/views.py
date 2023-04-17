from django.shortcuts import render
from django.http import Http404
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
    )
from .models import (
    Vehiculo,
)

from .serializers import (
    VehiculoSerializer,
    VehiculoLastSeenSerializer,
    VehiculoSerializerCreate
)

# class VehiculoView(APIView):
class VehiculoView(ListAPIView):

    # todo cambiar a queryset en vez del get
    serializer_class = VehiculoSerializer
    def get_queryset(self):
        nombre_equipo = self.request.GET.get('truck_name')
        id_mac = self.request.GET.get('id_mac')
        patente = self.request.GET.get('patente')
        if nombre_equipo: vehiculos = Vehiculo.objects.filter(nombre_equipo=nombre_equipo)
        elif patente: vehiculos = Vehiculo.objects.filter(patente=patente)
        elif id_mac: vehiculos = Vehiculo.objects.filter(id_mac=id_mac)
        else: vehiculos = Vehiculo.objects.all()
        return vehiculos


class VehiculoCreateView(CreateAPIView):
    serializer_class = VehiculoSerializerCreate


class VehiculoLastSeenView(UpdateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoLastSeenSerializer
    lookup_field = 'id_mac'
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "mobile number updated successfully"})
        else:
            return Response({"message": "failed", "details": serializer.errors})

class VehiculoUpdateView(UpdateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    lookup_field = 'id_mac'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "mobile number updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})


class VehiculoDeleteView(DestroyAPIView):

    serializer_class = VehiculoSerializer
    queryset = Vehiculo.objects.all()


class VehiculoRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = VehiculoSerializer
    queryset = Vehiculo.objects.all()

class VehiculoLSRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoLastSeenSerializer
    lookup_field = 'id_mac'
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "mobile number updated successfully"})
        else:
            return Response({"message": "failed", "details": serializer.errors})
