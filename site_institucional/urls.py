from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quemsomos', views.quemsomos, name='quemsomos'),
    path('servicos', views.servicos, name='servicos'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('depoimentos', views.depoimentos, name='depoimentos'),
    path('contato', views.portfolio, name='contato'),
]