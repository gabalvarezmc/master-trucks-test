from django.db import models
from django.utils import timezone
# Create your models here.


class RPrimer(models.Model):

    device_id = models.CharField(max_length=250)


class FileRPrimer(models.Model):

    equipo = models.ForeignKey(RPrimer, on_delete=models.CASCADE)
    file = models.FileField()
