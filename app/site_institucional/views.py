from app.site_institucional.forms import ContatoForm
from app.site_institucional.models import Contato
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
def index(request):
    # return render(request, 'index.html')


# def form_contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = ContatoForm()
    return render(request, 'index.html', {'form' : form})
