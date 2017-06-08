from django.db import models
from general.models import Articulo
import settings

# Create your models here.


ESTADOS = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo')
)
class Puja_Inversa(models.Model):
    fecha_inicio = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    fecha_cierre = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    articulo = models.ForeignKey(Articulo)

class Ofertantes_Puja_Invertida(models.Model):
    vendedor = models.ForeignKey(User)
    puja_inversa = models.ForeignKey(Puja_Inversa)
    valor = models.DecimalField(max_digits = 12, decimal_places = 2)
