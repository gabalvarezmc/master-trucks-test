from django.db import models
from cliente.models import Pais
# Create your models here.


class CompaniaCelular(models.Model):
    nombre_compania = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_compania + ' ' + self.pais.nombre_pais


class MarcaVehiculo(models.Model):
    nombre_marca = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_marca


class TipoCamion(models.Model):
    tipo_camion = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_camion


class SistemaControl(models.Model):
    sistema_control = models.CharField(max_length=100)

    def __str__(self):
        return self.sistema_control


class ModeloVehiculo(models.Model):
    modelo_camion = models.CharField(max_length=100)

    def __str__(self):
        return self.modelo_camion



class Vehiculo(models.Model):

    ESTADO = [
        ('activo', 'ACTIVO'),
        ('inactivo', 'inactivo'),
    ]

    CLASIFICACION = [
        ('Camion Fabrica', 'Camion Fabrica')

    ]

    nombre_equipo = models.CharField(max_length=100)
    clasificacion = models.CharField(max_length=50, choices=CLASIFICACION)
    estado = models.CharField(max_length=20, choices=ESTADO)
    sistema_control = models.ForeignKey(SistemaControl, on_delete=models.CASCADE)
    # compania_celular1 = models.ForeignKey(CompaniaCelular, on_delete=models.CASCADE, related_name='')
    numero_celular1 = models.CharField(max_length=36)
    # compania_celular2 = models.ForeignKey(CompaniaCelular, on_delete=models.CASCADE, blank=True, null=True)
    numero_celular2 = models.CharField(max_length=36, blank=True, null=True)
    id_mac = models.CharField(max_length=256)
    modelo = models.ForeignKey(ModeloVehiculo, on_delete=models.CASCADE)
    marca = models.ForeignKey(MarcaVehiculo, on_delete=models.CASCADE)
    patente = models.CharField(max_length=100)
    leasing = models.BooleanField(default=True, blank=True, null=True)
    año = models.DateField()
    capacidad_total = models.FloatField()
    matriz = models.FloatField()
    nitrato_amonio = models.FloatField()
    vin = models.CharField(max_length=255)
    alto_desempeño = models.BooleanField()
    alto_tonelaje = models.BooleanField()
    capacidad_agente = models.BooleanField()
    last_seen = models.DateTimeField(blank=True, null=True)
    last_latitud = models.FloatField(blank=True, null=True)
    last_longitud = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nombre_equipo
