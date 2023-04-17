from django.db import models
from cliente.models import Faena, ZonaServicio
# Create your models here.



class TipoGeocerca(models.Model):
    nombre_tipo = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Tipo de Geocerca"
        verbose_name_plural = 'Tipos de Geocercas'
    def __str__(self):
        return self.nombre_tipo


class Geocerca(models.Model):
    nombre_geocerca = models.CharField(max_length=100)
    zona_servicio = models.ForeignKey(ZonaServicio, blank=True, null=True, on_delete=models.CASCADE)
    faena = models.ForeignKey(Faena, blank=True, null=True, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=512, blank=True, null=True)
    tipo_geocerca = models.ForeignKey(TipoGeocerca, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_geocerca


class PuntosGeocercas(models.Model):
    latitud = models.DecimalField(max_digits=10, decimal_places=6)
    longitud = models.DecimalField(max_digits=10, decimal_places=6)
    geocerca = models.ForeignKey(to=Geocerca, on_delete=models.CASCADE, blank=True, null=True,)


    class Meta:
        verbose_name = "Punto Geocerca"
        verbose_name_plural = "Puntos Geocercas"

    def __str__(self):
        return f'{self.id}: {self.geocerca} - ({self.latitud}, {self.longitud})'

