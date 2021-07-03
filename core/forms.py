from django import forms
from django.forms import ModelForm
from .models import contacto

class ContactoForm(ModelForm):
    class Meta:
        model = contacto
        fields = ['nombre','telefono','email','direccion','mensaje']