from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from subastasx import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import *
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.template import Context
from django import forms
from django.db.models import Sum
from django.db.models import Q
import time
from datetime import datetime
from django.utils import timezone
# Create your views here.
from django.db.models import Max
# Generates a "SELECT MAX..." statement
class ListaPuja(LoginRequiredMixin, ListView):
    model = Puja
    login_url = settings.LOGIN_URL
    def get_queryset(self):
        return Puja.objects.all().order_by('-fecha_cierre')

@login_required
def detalle_puja(request,pk):
    if request.method=='POST':
        form = CrearOfertantes_PujaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return returnpuja(request,pk)
    else:
        return returnpuja(request,pk)

def returnpuja(request,pk):
    puja = Puja.objects.get(pk=pk)
    if puja.fecha_cierre <= timezone.now().date():
        ofer = Ofertantes_Puja.objects.filter(puja=puja).aggregate(Max('valor'))
        try:
            puja.articulo.valor_de_participacion = round((ofer["valor__max"] * Decimal(0.02)),2)
        except:
            puja.articulo.valor_de_participacion = 0
        puja.estado = 'Inactivo'
        puja.save()
    pujantes = Ofertantes_Puja.objects.filter(puja=pk).order_by('-valor')
    form = CrearOfertantes_PujaForm(initial = {'comprador':request.user.pk, 'puja':puja})
    context = Context({'puja':puja, 'pujantes': pujantes,'form':form })
    return render(request, 'puja/puja_detalles.html', context)

@login_required
def CrearArticulo(request):
    if request.method=='POST':
        form = CrearArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save()
            Puja.objects.create(articulo=articulo, estado="Activo", fecha_cierre = request.POST["fecha_cierre"], pide_pujas=request.user)
            return HttpResponseRedirect(reverse('ListaPuja'))
        else:
            form = CrearArticuloForm(request.POST)
            return render(request, 'puja/articulo_form.html', {'form':form})
    else:
        form = CrearArticuloForm()
        return render(request, 'puja/articulo_form.html', {'form':form})
