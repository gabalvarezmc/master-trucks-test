from django.contrib import admin
from .models import *
# Register your models here.

class GeocercasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_geocerca', 'faena', 'tipo_geocerca')
class PuntosAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitud', 'longitud')
class TipoGeoercaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_tipo')

admin.site.register(PuntosGeocercas)
admin.site.register(Geocerca, GeocercasAdmin)
admin.site.register(TipoGeocerca, TipoGeoercaAdmin)
