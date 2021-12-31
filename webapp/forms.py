from django import forms 
from django.forms import ModelForm , EmailInput
#from django.forms import ModelForm , EmailInput
from webapp.models import Persona , Domicilio

class PersonaForm(ModelForm):

    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email' : EmailInput(attrs= {'type' : 'email'}) 
        }

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'no_calle' : forms.TextInput(attrs={'type' : 'number'}) 
            }