from django.urls import path
from . import views

urlpatterns = [
    # path('geocerca/list', views.GeocercaView.as_view(), name='list_geocerca'),
    # path('geodata/list', views.GeoDataView.as_view(), name='list_geodata'),
    path('geodata/create', views.create_or_update_geodata, name='create_geodata')

]