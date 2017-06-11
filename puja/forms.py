from django.forms import ModelForm
from django import forms
from .forms import *
from .models import *
from general.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin.widgets import AdminDateWidget

class CrearOfertantes_PujaForm(ModelForm):
    class Meta:
        model = Ofertantes_Puja
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CrearOfertantes_PujaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['comprador'].widget = forms.HiddenInput()
        self.fields['puja'].widget = forms.HiddenInput()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.add_input(Submit('submit', 'Pujar'))

class CrearArticuloForm(ModelForm):
    fecha_cierre = forms.DateField()
    class Meta:
        model = Articulo
        fields = ["nombre","descripcion","cantidad","precio","valor_de_participacion","valor_de_envio","tiempo_de_entrega","fecha_cierre","image"]
    def __init__(self, *args, **kwargs):
        super(CrearArticuloForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['valor_de_participacion'].widget = forms.HiddenInput()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.add_input(Submit('submit', 'Agregar'))
