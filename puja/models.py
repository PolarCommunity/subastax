from django.db import models
from general.models import Articulo
import settings
# Create your models here.


ESTADOS = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
)

class Puja(models.Model):
    fecha_cierre = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    estado = models.CharField(max_length=10, choices=ESTADOS)
    articulo = models.ForeignKey(Articulo)

class Ofertantes_Puja(models.Model):
    comprador = models.ForeignKey(User)
    puja_inversa = models.ForeignKey(Puja_Inversa)
    valor = models.DecimalField(max_digits = 12, decimal_places = 2)
