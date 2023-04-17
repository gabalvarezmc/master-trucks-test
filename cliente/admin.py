from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from .models import *
# Register your models here.

admin.site.register(Pais)
admin.site.register(Cliente)
admin.site.register(Faena)
admin.site.register(Operacion)
admin.site.register(Fase)
admin.site.register(Banco)
admin.site.register(Poligono)
admin.site.register(Malla)
admin.site.register(Pozo)
admin.site.register(Molino)
admin.site.register(Chancador)
admin.site.register(ZonaServicio)