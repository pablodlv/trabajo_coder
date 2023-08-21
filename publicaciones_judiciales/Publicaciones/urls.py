from django.urls import path
from .views import *

urlpatterns = [
    path('remates/', remates, name='remates'),
    path('carga_remates/', cargar_rema, name='carga_remates'),
    path('licitaciones/', licitaciones, name='licitaciones'),
    path('carga_licitaciones/', cargar_lic, name='carga_licitaciones'),
    path('martilleros/', martilleros, name='martilleros'),
    path('carga_martilleros/', cargar_mart, name='carga_martilleros'),
    path('operadores/', operadores, name='operadores'),
    path('clientes/', clientes, name='clientes'),
    path('carga_clientes/', cargar_cli, name='carga_clientes'),
]