from doctest import REPORT_UDIFF
from math import ceil
from rest_framework import viewsets   
from .models import Asiento, Boleto, HorarioXTrayecto, Ruta, Usuario, Bus, Trayecto
from .serializers import AsientoSerializer, BoletoSerializer, HorarioXTrayectoSerializer, RutaSerializer, UsuarioSerializer, BusSerializer, TrayectoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


## ModelViewSets

class ChoferModelViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(esChofer = True)
    serializer_class = UsuarioSerializer
    lookup_value_regex = "[^/]+"  


class PasajeroModelViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(esChofer = False)
    serializer_class = UsuarioSerializer
    lookup_value_regex = "[^/]+"  

class BusModelViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class TrayectoViewSet(viewsets.ModelViewSet):
    queryset = Trayecto.objects.all()
    serializer_class = TrayectoSerializer

class AsientoViewSet(viewsets.ModelViewSet):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer

class BoletoViewSet(viewsets.ModelViewSet):
    queryset = Boleto.objects.all()
    serializer_class = BoletoSerializer

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

class HorarioXTrayectoViewSet(viewsets.ModelViewSet):
    queryset = HorarioXTrayecto.objects.all()
    serializer_class = HorarioXTrayectoSerializer


## APIVIEWS
class PromedioPasajeros(APIView):
    def get(self, request, fk, pk, format=None):
        boletos = Boleto.objects.filter(trayecto=pk).count()
        horarios = HorarioXTrayecto.objects.filter(trayecto=pk).count()
        if(horarios == 0):
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            resultado = ceil(boletos/horarios)
            return Response(resultado, status=status.HTTP_200_OK)
    
class CapacidadVendida(APIView):
    def get(self, request, fk, pk, format=None):
        available = []
        horarios =  HorarioXTrayecto.objects.filter(trayecto=pk).values('id')
        for horario in horarios:
            cantidad_boletos = Boleto.objects.filter(horario=horario['id']).count()            
            if cantidad_boletos > fk:
                toPush = HorarioXTrayecto.objects.filter(id=horario['id'])[:1].get()
                available.append(toPush)
        serializer = HorarioXTrayectoSerializer(available, many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)