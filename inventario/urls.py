from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
################################## MODEL VIEW SET ######################################
router = DefaultRouter()
router.register (r"dispositivos",views.DispositivoViewSet)
router.register (r"asignacion",views.AsignacionViewSet)
router.register (r"usuario",views.UsuarioViewSet)
router.register (r"tipodispositivo",views.TipodispositivoViewSet)

################################## URLS INVENTARIO #####################################

urlpatterns =[
        path("contact/<str:name>",views.contact,name="contact"),
        path("dispositivos",views.Dispositivo,name="dispositivos"),
        path("asignacion",views.Asignacion,name="asignacion"),
        path("usuario",views.Usuario,name="usuario"),
        path("tipodispositivo",views.Tipodispositivo,name="tipodispositivo"),
        path("tipodispositivo/contador",views.Tipodispositivo_count,name="tipodispositivocount"), #CUSTOM VIEW
        path("",include(router.urls)),
]