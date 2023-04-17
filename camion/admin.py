from django.contrib import admin

from .models import *
# Register your models here.
# dmin.site.register(Vehiculo)

admin.site.register(CompaniaCelular)
admin.site.register(MarcaVehiculo)
admin.site.register(TipoCamion)
admin.site.register(SistemaControl)
admin.site.register(ModeloVehiculo)

class VehiculoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_equipo',
        'id_mac',
        'patente'
    )

admin.site.register(Vehiculo, VehiculoAdmin)
