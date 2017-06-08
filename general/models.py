from django.db import models
from django.contrib.auth.models import User
from datetime import date
from subastasx import settings

# Create your models here.

class Direccion(models.Model):
    user = models.OneToOneField(User)
    direccion = models.CharField(max_length=50)

class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=254)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, null=True, blank=True, verbose_name=("Imagen"))
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits = 12, decimal_places = 2)
    valor_de_participacion = models.DecimalField(max_digits = 12, decimal_places = 2)
    valor_de_envio = models.DecimalField(max_digits = 12, decimal_places = 2)
    tiempo_de_entrega = models.IntegerField()

class Tarjeta(models.Model):
    no_de_tarjeta = models  .CharField(max_length=15)
    nivel_de_tarjeta = models.CharField(max_length=15)
    usuario = models.ForeignKey(User)
