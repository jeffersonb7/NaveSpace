from app.site_institucional.forms import ContatoForm
from app.site_institucional.models import Contato
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
    return render(request, 'index.html', {'form': form})
