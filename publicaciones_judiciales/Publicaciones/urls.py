from django.urls import path
from .views import *

urlpatterns = [
    path('remates/', remates, name='remates'),
    path('carga_remates/', cargar_rema, name='carga_remates'),
    path('licitaciones/', licitaciones, name='licitaciones'),
    path('carga_licitaciones/', cargar_lic, name='carga_licitaciones'),
    path('martilleros/', martilleros, name='martilleros'),
    path('carga_martilleros/', cargar_mart, name='carga_martilleros'),
    path('clientes/', clientes, name='clientes'),
    path('carga_clientes/', cargar_clie, name='carga_clientes'),
    path('operadores/', operadores, name='operadores'),
    path('carga_operadores/', cargar_opera, name='carga_operadores'),
    path('busqueda_remates/', busquedaRemate, name='busqueda_remates'),
    path('remates_encontrados/', busquedaBien, name='buscar_rema'),
    path('busqueda_licitaciones/', busquedaLicitacion, name='busqueda_licitaciones'),
    path('licitaciones_encontradas/', busquedaObjeto, name='buscar_lici'),
]