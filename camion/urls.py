from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.VehiculoView.as_view(), name='vehiculo_view'),
    path("create/", views.VehiculoCreateView.as_view(), name='vehiculo_create'),
    path("updatelastseen/<id_mac>/", views.VehiculoLastSeenView.as_view(), name='vehiculo_update_lastseen'),
    path("update/<id_mac>/", views.VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path("delete/<pk>/", views.VehiculoDeleteView.as_view(), name='vehiculo_delete'),
    path("modificar/<pk>/", views.VehiculoRetrieveUpdateView.as_view(), name='vehiculo_modificar'),
    path("modificar2/<id_mac>/", views.VehiculoLSRetrieveUpdateView.as_view(), name='vehiculo_modificar2'),
]