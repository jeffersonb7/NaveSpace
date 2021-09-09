from django import forms
from django.forms import fields
from .models import Contato

class ContatoForm(forms.ModelForm):

    class Meta:
        model = Contato
        fields = ('nome', 'telefone', 'email', 'mensagem')