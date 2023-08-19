from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def remates(request):
    return render(request,'remates.html')

def licitaciones(request):
    return render(request,'licitaciones.html')

def operadores(request):
    return render(request,'operadores.html')

def martilleros(request):
    return render(request,'martilleros.html')

def clientes(request):
   return render(request,'clientes.html')
