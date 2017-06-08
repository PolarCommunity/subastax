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
    paginate_by = 50
    login_url = settings.LOGIN_URL

@login_required
def crear_puja(request):
    if request.method == 'POST':
        form = CrearPujaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ListaPuja')
        else:
            print("no sirve")
    else:
        form = CreateCuentaForm(initial = {'banco':banco.pk})
        form.fields['banco'].widget = forms.HiddenInput()
        context = Context({'form':form})
        return render(request, 'puja/puja_form.html', context)
