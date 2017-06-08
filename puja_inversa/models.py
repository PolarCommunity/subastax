from django.db import models
from general.models import Articulo
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


ESTADOS = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo')
)
class Puja_Inversa(models.Model):
    fecha_inicio = models.DateField(default=date.today)
    fecha_cierre = models.DateField(default=date.today)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    articulo = models.ForeignKey(Articulo)

class Ofertantes_Puja_Invertida(models.Model):
    vendedor = models.ForeignKey(User)
    puja_inversa = models.ForeignKey(Puja_Inversa)
    valor = models.DecimalField(max_digits = 12, decimal_places = 2)
