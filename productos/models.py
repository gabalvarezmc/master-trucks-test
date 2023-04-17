from django.db import models

# Create your models here.


class Producto(models.Model):

    nombre_producto = models.CharField(max_length=100)

