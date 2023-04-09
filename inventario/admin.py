from django.contrib import admin

# Register your models here.
from .models import Tipodispositivo
from .models import Dispositivo
from .models import Asignacion
from .models import Usuario
admin.site.register(Tipodispositivo)


admin.site.register(Usuario)

class DispositivoAdmin(admin.ModelAdmin):
    list_display=("nombre","ordendecompra","descripcion")
    ordering=["nombre"]
    search_fields=["nombre"]
    list_filter=["ordendecompra"]

admin.site.register(Dispositivo,DispositivoAdmin)

class AsignacionAdmin(admin.ModelAdmin):
    list_display=("descripcion","fecha","dispositivo")
    ordering=["descripcion"]
    search_fields=["descripcion"]
    list_filter=["dispositivo__ordendecompra"]

admin.site.register(Asignacion,AsignacionAdmin)
