from django.core.exceptions import ValidationError

def validarnocero (value):
    if value <=0:
        raise ValidationError(
            '%(value)s debe ser mayor a cero', params={'value':value},
        )
    

def validarsologmail (value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError(
            '%(value)s solo se aceptan correos de gmail', params={'value':value},
        )
            
