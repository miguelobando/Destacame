from django import views
from api.models import Bus
from .views import AsientoViewSet, ChoferModelViewSet, BusModelViewSet
from .views import HorarioXTrayectoViewSet, PasajeroModelViewSet, RutaViewSet
from .views import TrayectoViewSet, BoletoViewSet, PromedioPasajeros
from .views import CapacidadVendida
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('choferes', ChoferModelViewSet, basename='Chofer')
router.register('pasajeros', PasajeroModelViewSet, basename='Pasajero')
router.register('buses', BusModelViewSet, basename='Bus')
router.register('trayectos', TrayectoViewSet, basename='Trayecto')
router.register('asientos', AsientoViewSet, basename='Asiento')
router.register('boletos', BoletoViewSet, basename='Boleto')
router.register('rutas', RutaViewSet, basename='Ruta')
router.register('horarios', HorarioXTrayectoViewSet, basename='HorarioxTrayecto')
urlpatterns = router.urls

urlpatterns.append(path('trayectos/<int:pk>/promediopasajeros/<int:fk>/',PromedioPasajeros.as_view()))
urlpatterns.append(path('trayectos/<int:pk>/capacidad/<int:fk>/',CapacidadVendida.as_view()))
