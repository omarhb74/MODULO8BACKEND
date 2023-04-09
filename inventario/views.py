from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Dispositivo
from .models import Asignacion
from .models import Usuario
from .models import Tipodispositivo
from .serializers import Dispositivoserializer
from .serializers import Asignacionserializer
from .serializers import Usuarioserializer
from .serializers import Tipodispositivoserializer

# Create your views here.

def helloworld (request):
    return HttpResponse('Hello World')

def contact (request,name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

############################ MODEL VIEW SET###########################
class DispositivoViewSet (viewsets.ModelViewSet):
    queryset=Dispositivo.objects.all()
    serializer_class=Dispositivoserializer


class AsignacionViewSet (viewsets.ModelViewSet):
    queryset=Asignacion.objects.all()
    serializer_class=Asignacionserializer

class UsuarioViewSet (viewsets.ModelViewSet):
    queryset=Usuario.objects.all()
    serializer_class=Usuarioserializer

class TipodispositivoViewSet (viewsets.ModelViewSet):
    queryset=Tipodispositivo.objects.all()
    serializer_class=Tipodispositivoserializer

############################ CUSTOM API #################################

@api_view (["GET"])
def Tipodispositivo_count (request):
    try:
        cantidad = Tipodispositivo.objects.count()
        print(cantidad)
        return JsonResponse({
            "cantidad":cantidad


        },safe=False,status=200,)
    except Exception as e:
        return JsonResponse ({"mensaje error":str (e)},status=400)

        
