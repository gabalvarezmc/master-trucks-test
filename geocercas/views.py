from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
    )
from .models import (
    PuntosGeocercas,
    Geocerca,
    TipoGeocerca
)

from .serializers import (
    GeocercasSerializer,
    GeocercaSerializerCreate,
    GeocercaSerializerUpdate,
    GeoDataSerializerCreate,
    GeoDataSerializerList,
    GeoDataSerializerAll,
    GeoDataSerializerUpdate,
    GeoTypeSerializer
)

################# GEOCERCA ####################
class GeocercaListView(ListAPIView):
    serializer_class = GeocercasSerializer
    queryset = Geocerca.objects.all()


class GeocercaCreateView(CreateAPIView):
    serializer_class = GeocercaSerializerCreate
    queryset = Geocerca.objects.all()


class GeocercaDeleteView(DestroyAPIView):

    serializer_class = GeocercasSerializer
    queryset = Geocerca.objects.all()


class GeocercaRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = GeocercaSerializerUpdate
    queryset = Geocerca.objects.all()

################# PUNTOS GEOCERCA ####################

class GeoDataListView(ListAPIView):
    serializer_class = GeoDataSerializerList

    def get_queryset(self):
        queryset = PuntosGeocercas.objects.all()
        nombre_faena = self.request.query_params.get('faena')
        zona_servicio = self.request.query_params.get('zona-servicio')

        if nombre_faena:
            queryset = queryset.filter(geocerca__faena__nombre_faena=nombre_faena)

        elif zona_servicio:
            queryset = queryset.filter(geocerca__zona_servicio__nombre_zona=zona_servicio)
        return queryset


class GeoDataCreate(CreateAPIView):
    serializer_class = GeoDataSerializerCreate
    queryset = PuntosGeocercas.objects.all()


class GeoDataDeleteView(DestroyAPIView):

    serializer_class = GeoDataSerializerAll
    queryset = PuntosGeocercas.objects.all()


class GeoDataRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = GeoDataSerializerUpdate
    queryset = PuntosGeocercas.objects.all()

################# TIPOS GEOCERCA ####################

class GeoTypeListView(ListAPIView):
    serializer_class = GeoTypeSerializer
    queryset = TipoGeocerca.objects.all()


class GeoTypeCreateView(CreateAPIView):
    serializer_class = GeoTypeSerializer
    queryset = TipoGeocerca.objects.all()


class GeoTypeDeleteView(DestroyAPIView):

    serializer_class = GeoTypeSerializer
    queryset = TipoGeocerca.objects.all()


class GeoTypeRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = GeoTypeSerializer
    queryset = TipoGeocerca.objects.all()