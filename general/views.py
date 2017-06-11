from django.shortcuts import render, redirect
from decimal import Decimal
from .models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django import forms
from django.views.generic import *
from django.contrib import auth
from subastasx import settings
from django.db.models import Q
from .forms import *
from django.contrib.auth.models import User

# Create your views here.
def Register(request):
    if request.method == "GET":
        return render(request, 'usuario/register.html')
    elif request.method == "POST":
            username = request.POST["username"]
            password = "123prueba"
            email = request.POST["email"]
            auth.models.User.objects.create_user(username, email, password).save()
            user = User.objects.get(username=request.POST['username'])
            user.first_name=request.POST['nombres']
            user.last_name=request.POST['apellidos']
            Direccion.objects.create(user=user,direccion=request.POST['direccion'])
            Tarjeta.objects.create(usuario=user,no_de_tarjeta=request.POST['tarjeta'])
            user.save()
            return render(request, "password.html")




def Home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        if request.method == "GET":
            return render(request, "usuario/login.html")
        elif request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    if(user.last_login == None):
                        auth.login(request, user)
                        return redirect(reverse('ChangePassword'))
                    auth.login(request, user)
                    next = "/home"
                    if "next" in request.GET:
                        next = request.GET["next"]
                    if next == None or next == "":
                        next = "/"
                    return redirect(next)
                else:
                    return render(request, "usuario/login.html", {"mensaje": "Tu cuenta ha sido deshabilitada"})
            else:
                return render(request, "usuario/login.html", {"mensaje": "Usuario o contraseña incorrecta"})

@login_required
def ChangePassword(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            password = request.POST['password1']
            user = User.objects.get(username=str(request.user.username))
            if user.is_active:
                user.set_password(password)
                user.save()
                user = auth.authenticate(username=request.user.username, password=password)
                return redirect(reverse('home'))
        else:
            return render(request, 'change-password.html')
    else:
        return render(request, 'change-password.html')

@login_required
def Logout(request):
    auth.logout(request)
    return redirect("/")
