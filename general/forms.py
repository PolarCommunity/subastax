from django.forms import ModelForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

class CrearArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CrearArticuloForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['saldo'].widget = forms.HiddenInput()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.add_input(Submit('submit', 'Agregar'))
