from django.forms import ModelForm
from django import forms
from .forms import *
from .models import *
from general.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin.widgets import AdminDateWidget

class CrearPujaForm(ModelForm):
    class Meta:
        model = Puja
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CrearPujaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['articulo'].widget = forms.HiddenInput()
        self.fields['estado'].widget = forms.HiddenInput()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.add_input(Submit('submit', 'Agregar'))

class CrearArticuloForm(ModelForm):
    fecha_cierre = forms.DateField()
    class Meta:
        model = Articulo
        fields = '__all__'
        widgets = {
            'date': AdminDateWidget(),
        }
    def __init__(self, *args, **kwargs):
        super(CrearArticuloForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.add_input(Submit('submit', 'Agregar'))
