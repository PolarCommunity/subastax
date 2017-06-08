from django.db import models
from general.models import Articulo
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


ESTADOS = (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
)

class Puja(models.Model):
    fecha_cierre = models.DateField(default=date.today)
    estado = models.CharField(max_length=10, choices=ESTADOS)
    articulo = models.ForeignKey(Articulo)

class Ofertantes_Puja(models.Model):
    comprador = models.ForeignKey(User)
    puja = models.ForeignKey(Puja)
    valor = models.DecimalField(max_digits = 12, decimal_places = 2)
