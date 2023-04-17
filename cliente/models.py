from django.db import models

# Create your models here.


class Pais(models.Model):
    nombre_pais = models.CharField(max_length=100)
    acronimo = models.CharField(max_length=40, null=True, blank=True)
    lenguaje = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nombre_pais


class Cliente(models.Model):

    nombre_cliente = models.CharField(max_length=100)
    foto_cliente = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.nombre_cliente


class Faena(models.Model):

    nombre_faena = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    foto_faena = models.FileField(blank=True, null=True)

    class Meta:
        verbose_name = "Faena"
        verbose_name_plural = "Faenas"

    def __str__(self):
        return "{0} - {1}".format(self.nombre_faena, self.pais)


class Operacion(models.Model):

    nombre_operacion = models.CharField(max_length=100)
    faena = models.ForeignKey(Faena, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Operacion"
        verbose_name_plural = "Operaciones"

    def __str__(self):
        return self.nombre_operacion


class Fase(models.Model):
    nombre_fase = models.CharField(max_length=100)
    operacion = models.ForeignKey(Operacion, on_delete=models.CASCADE)
    planos = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.nombre_fase


class Banco(models.Model):
    identificador_banco = models.CharField(max_length=255)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)
    planos = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.identificador_banco


class Poligono(models.Model):
    identificador_poligono = models.CharField(max_length=255)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    plano_poligono = models.FileField(blank=True, null=True)
    def __str__(self):
        return self.identificador_poligono


class Malla(models.Model):
    identificador_malla = models.CharField(max_length=255)
    poligono = models.ForeignKey(Poligono, on_delete=models.CASCADE)
    plano_malla = models.FileField(blank=True, null=True)
    def __str__(self):
        return self.identificador_malla


class Pozo(models.Model):
    identificador_pozo = models.CharField(max_length=255)
    latitud = models.FloatField(blank=True)
    longitud = models.FloatField(null=True)
    def __str__(self):
        return self.identificador_pozo


class ZonaServicio(models.Model):

    nombre_zona = models.CharField(max_length=100)
    tipo_zona = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Zona de Servicio"
        verbose_name_plural = "Zonas de Servicios"
    def __str__(self):
        return self.nombre_zona
        

class Chancador(models.Model):
    faena = models.ForeignKey(Faena, on_delete=models.CASCADE)
    modelo_chancador = models.CharField(max_length=255)
    setting_objetivo = models.FloatField(blank=True)
    nombre_chancador = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Chancador"
        verbose_name_plural = 'Chancadores'
    def __str__(self):
        return self.nombre_chancador


class Molino(models.Model):
    nombre_molino = models.CharField(max_length=255)
    faena = models.ForeignKey(Faena, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Molino"
        verbose_name_plural = 'Molinos'
    def __str__(self):
        return self.nombre_molino
