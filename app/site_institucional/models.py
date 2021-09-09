from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    mensagem = models.TextField()

class Servico(models.Model):
    nome_servico = models.CharField(max_length=100)