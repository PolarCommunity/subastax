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

# Create your views here.

class ListaPuja(LoginRequiredMixin, ListView):
    model = Puja
    login_url = settings.LOGIN_URL

class CrearPuja(LoginRequiredMixin, CreateView):
    model = Puja
    form_class = CrearPujaForm
    login_url = settings.LOGIN_URL
    template_name = 'puja/puja_form.html'
    success_url = reverse_lazy('CrearPuja')

@login_required
def CreatePuja(request, pk):
    articulo = Articulo.objects.get(pk=pk)
    if request.method=='POST':
        form = CrearPujaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ListaPuja'))
    else:
        form = CrearPujaForm(initial = {'articulo':pk})
        return render(request, 'puja/puja_form.html', {'form':form,'articulo':articulo})

class CrearArticulo(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = CrearArticuloForm
    login_url = settings.LOGIN_URL
    template_name = 'puja/articulo_form.html'
    def get_success_url(self):
        return reverse('CreatePuja',args=(self.object.id,))
