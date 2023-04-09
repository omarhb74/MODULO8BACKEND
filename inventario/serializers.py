from rest_framework import serializers
from .models import Dispositivo
from .models import Asignacion
from .models import Usuario
from .models import Tipodispositivo

#################################### SERIALIZADORES DE 4 MODELOS ###############################

class Dispositivoserializer (serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = "__all__"



class Asignacionserializer (serializers.ModelSerializer):
    class Meta:
        model = Asignacion
        fields = "__all__"
        read_only_fields=('created_at',)

class Usuarioserializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
        read_only_fields=('created_at',)

class Tipodispositivoserializer (serializers.ModelSerializer):
    class Meta:
        model = Tipodispositivo
        fields = "__all__"
        read_only_fields=('created_at',)
