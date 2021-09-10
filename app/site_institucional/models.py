from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11, null="True", blank="True")
    email = models.EmailField(max_length=254)
    mensagem = models.TextField()
    
    def __str__(self):
        return self.nome

class Home(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)

    def __str__(self):
        return self.titulo

class Servico(models.Model):
    nome_servico = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_servico

class Sobre(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    img = models.ImageField(upload_to="sobre_nos", null="True" , blank="True")
    
    def __str__(self):
        return self.titulo

class Produto(models.Model): #seção portfolio 
    imgs = models.ImageField(upload_to="produto", null="True" , blank="True")

class Depoimento(models.Model):
    img = models.ImageField(upload_to="depoimento", null="True" , blank="True")
    nome = models.CharField(max_length=100)
    mensagem = models.TextField(max_length=300)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=30)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=100)