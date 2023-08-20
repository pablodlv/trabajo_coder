from django.urls import path
from .views import *

urlpatterns = [
    path('remates/', remates, name='remates'),
    path('licitaciones/', licitaciones, name='licitaciones'),
    path('clientes/', clientes, name='clientes'),
    path('martilleros/', martilleros, name='martilleros'),
    path('operadores/', operadores, name='operadores'), 
]