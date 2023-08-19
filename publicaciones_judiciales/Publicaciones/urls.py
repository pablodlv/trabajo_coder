from django.urls import path
from .views import *

urlpatterns = [
    path('remates/', remates),
    path('licitaciones/', licitaciones),
    path('clientes/', clientes),
    path('martilleros/', martilleros),
    path('operadores/', operadores), 
]