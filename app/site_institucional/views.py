from app.site_institucional.forms import ContatoForm
from app.site_institucional.models import Contato, Depoimento, Endereco, Home, Produto, Servico, Sobre
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('index') 
    else:
        form = ContatoForm()
    

    home = Home.objects.last()
    servicos = Servico.objects.all()
    sobre = Sobre.objects.last()
    depoimentos = Depoimento.objects.all()
    endereco = Endereco.objects.last()
    produtos = Produto.objects.all()

    context = {
        'home': home,
        'form': form,
        'servicos': servicos,
        'sobre': sobre,
        'endereco': endereco,
        'depoimentos': depoimentos,
        'produtos' : produtos
    }
    return render(request, 'index.html', context)
