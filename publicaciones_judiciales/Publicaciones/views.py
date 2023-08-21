from django.shortcuts import render
from .models import Remate, Licitacion, Martillero, Cliente, Operador
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def remates(request):
    lista_remates=Remate.objects.all()
    return render(request,'remates.html', {'listado_remates':lista_remates})

def licitaciones(request):
    lista_licitaciones=Licitacion.objects.all()
    return render(request,'licitaciones.html', {'listado_licitaciones':lista_licitaciones})

def operadores(request):
    lista_operadores=Operador.objects.all()
    return render(request,'operadores.html', {'listado_operadores':lista_operadores})

def martilleros(request):
    lista_martilleros=Licitacion.objects.all()
    return render(request,'martilleros.html', {'listado_martilleros':lista_martilleros})

def clientes(request):
   lista_clientes=Cliente.objects.all()
   return render(request,'clientes.html', {'listado_clientes':lista_clientes})

# Crud 

def cargar_rema(request):
    if request.method=='POST':
        bien=request.POST['bien']
        base=request.POST['base']
        fecha=request.POST['fecha']
        lugar=request.POST['lugar']
        remate=Remate(bien=bien,base=base,fecha=fecha,lugar=lugar)
        remate.save()
        return render(request,'remates_formulario.html', {'mensaje':'Remate creado'})
    else:
        return render(request,'remates_formulario.html')

def cargar_lic(request):
    if request.method=='POST':
        objeto=request.POST['objeto']
        referencia=request.POST['referencia']
        fecha=request.POST['fecha']
        link=request.POST['link']
        licitacion=Licitacion(objeto=objeto,referencia=referencia,fecha=fecha,link=link)
        licitacion.save()
        return render(request,'licitaciones_formulario.html', {'mensaje':'Licitación creada'})
    else:
        return render(request,'licitaciones_formulario.html')
    
def cargar_mart(request):
    if request.method=='POST':
        martillero=Martillero(request.POST['nombre'],(request.POST['apellido'],(request.POST['matricula'],(request.POST['email']))))
        martillero.save()
        return render(request, "martilleros.html", {'mensaje':'Martillero cargado'})
    else:
        return render(request,"martilleros.html")
