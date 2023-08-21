from django.urls import path
from .views import *

urlpatterns = [
    path('remates/', remates, name='remates'),
    path('licitaciones/', licitaciones, name='licitaciones'),
    path('clientes/', clientes, name='clientes'),
    path('martilleros/', martilleros, name='martilleros'),
    path('operadores/', operadores, name='operadores'),
    path('remates_formulario/', cargar_rema, name='carga_remates'),
    path('licitaciones_formulario/', cargar_lic, name='carga_licitaciones'),
    path('carga_martilleros/', cargar_mart, name='carga_martilleros'),
]