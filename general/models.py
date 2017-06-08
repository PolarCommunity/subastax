from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Direccion(models.Model):
    user = models.OneToOneField(User)
    sede = models.CharField(max_length=50)

class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=254)
    image = models.ImageField(upload_to='articulo/', null=True, blank=True, verbose_name=_("Imagen"))
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits = 12, decimal_places = 2)
    valor_de_participacion = models.DecimalField(max_digits = 12, decimal_places = 2)
    valor_de_envio = models.DecimalField(max_digits = 12, decimal_places = 2)
    tiempo_de_entrega = models.IntegerField()

class Tarjeta(models.Model):
    no_de_tarjeta = models  .CharField(max_length=15)
    nivel_de_tarjeta = models.CharField(max_length=15)
    usuario = models.ForeignKey(User)
