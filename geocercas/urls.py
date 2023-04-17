from django.urls import path

from . import views

urlpatterns = [
    # GEOCERCAS
    path("geocerca/list/", views.GeocercaListView.as_view(), name='Geocerca_view'),
    path("geocerca/create/", views.GeocercaCreateView.as_view(), name='Geocerca_create'),
    path("geocerca/delete/<pk>/", views.GeocercaDeleteView.as_view(), name='Geocerca_delete'),
    path("geocerca/modificar/<pk>/", views.GeocercaRetrieveUpdateView.as_view(), name='Geocerca_modificar'),
    # GEODATA
    path('geodata/list/', views.GeoDataListView.as_view(), name='list_geodata'),
    path('geodata/create/', views.GeoDataCreate.as_view(), name='create_geodata'),
    path("geodata/delete/<pk>/", views.GeoDataDeleteView.as_view(), name='geodata_delete'),
    path("geodata/modificar/<pk>/", views.GeoDataRetrieveUpdateView.as_view(), name='geodata_modificar'),
    # GEOTYPE
    path('geotype/list/', views.GeoTypeListView.as_view(), name='list_geotype'),
    path('geotype/create/', views.GeoTypeCreateView.as_view(), name='create_geotype'),
    path("geotype/delete/<pk>/", views.GeoTypeDeleteView.as_view(), name='geotype_delete'),
    path("geotype/modificar/<pk>/", views.GeoTypeRetrieveUpdateView.as_view(), name='geotype_modificar'),
]