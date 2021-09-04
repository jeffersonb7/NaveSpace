from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

# def quemsomos(request):
#     return render(request, '')

# def servicos(request):
#     return render(request, '')

# def portfolio(request):
#     return render(request, '')

# def depoimentos(request):
#     return render(request, '')

# def contato(request):
#     return render(request, '')