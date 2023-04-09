from django.db import models
from .validators import validarnocero
from .validators import validarsologmail
from django.core.validators import EmailValidator



# Create your models here.

################################### MODELOS ##################################

class Tipodispositivo(models.Model):
      nombre=models.CharField(max_length=255)

      def __str__(self):
            return self.nombre
    
  




class Dispositivo(models.Model):
    
    nombre=models.CharField(max_length=100)
    ordendecompra=models.CharField(max_length=10,blank=False)
    descripcion=models.TextField(blank=True)
    fechavencimientogarantia=models.DateTimeField(null=True)
    precio=models.DecimalField(decimal_places=2,max_digits=10,null=True,validators=[validarnocero]) #CUSTOM VALIDATOR
    dispositivo=models.ForeignKey(Tipodispositivo,on_delete=models.CASCADE)
    
 


class Usuario(models.Model):
    
    nombre=models.CharField(max_length=100)
    cedula=models.TextField(blank=False)
    fecharegistro=models.DateTimeField(null=False)
    email=models.EmailField(max_length=70,blank=True,validators=[validarsologmail])
    

    
    
                    


class Asignacion(models.Model):
    
    
    descripcion=models.TextField(blank=True)
    estado=models.BooleanField(null=False,default=True)
    fecha=models.DateTimeField(auto_now_add=True)
    dispositivo =models.ForeignKey(Dispositivo,on_delete=models.CASCADE)
    cliente=models.ForeignKey(Usuario,on_delete=models.CASCADE)


