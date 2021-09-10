from django.contrib import admin
from .models import Contato, Depoimento, Endereco, Home, Produto, Servico, Sobre
# Register your models here.

admin.site.register(Contato)
admin.site.register(Servico)
admin.site.register(Home)
admin.site.register(Sobre)
admin.site.register(Produto)
admin.site.register(Depoimento)
admin.site.register(Endereco)