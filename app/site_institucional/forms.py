from django import forms
from django.forms import fields
from .models import Contato

class ContatoForm(forms.ModelForm):

    class Meta:
        model = Contato
        fields = ('nome', 'telefone', 'email', 'text')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control nombre', 'placeholder': 'joão da silva', 'type': 'text', 'name':'nombre' }),
            'telefone': forms.EmailInput(attrs={'class': 'form-control nombre', 'placeholder': '40028922', 'type': 'tel', 'name':'nombre' }),
            'email': forms.TextInput(attrs={'class': 'form-control nombre', 'placeholder': 'joão@gmail.com', 'id': 'email', 'type': 'email', 'name' : 'email'}),
            'text': forms.Textarea(attrs={'class': 'form-control nombre', 'placeholder': 'Todos forram efetivados', 'id': 'inputmensagem'})
        }