from django.shortcuts import render
from .models import Remate, Licitacion, Martillero, Cliente, Operador
from django.http import HttpResponse
from .forms import licitacionForm, clienteForm, martilleroForm, operadorForm, remateForm

# Creo las vistas.

def inicio(request):
    return render(request, 'inicio.html')

def remates(request):
    lista_remates=Remate.objects.all()
    return render(request,'remates.html', {'listado_remates':lista_remates})

def licitaciones(request):
    lista_licitaciones=Licitacion.objects.all()
    return render(request,'licitaciones.html', {'listado_licitaciones':lista_licitaciones})

def martilleros(request):
    lista_martilleros=Martillero.objects.all()
    return render(request,'martilleros.html', {'listado_martilleros':lista_martilleros})

def clientes(request):
    lista_clientes=Cliente.objects.all()
    return render(request,'clientes.html', {'listado_clientes':lista_clientes})

def operadores(request):
    lista_operadores=Operador.objects.all()
    return render(request,'operadores.html', {'listado_operadores':lista_operadores})

# Vistas de los formularios

def cargar_rema(request):
    if request.method=='POST':
        form=remateForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            bien=info['bien']
            base=info['base']
            fecha=info['fecha']
            lugar=info['lugar']
            remate=Remate(bien=bien,base=base,fecha=fecha,lugar=lugar)
            remate.save()
            remate_formulario=remateForm()
            return render(request,'carga_remates.html', {'mensaje':'Remate cargado', 'formulario':remate_formulario})
        return render(request,'carga_remates.html', {'mensaje':'Datos inválidos'})
    else:
        remate_formulario=remateForm()
        return render(request,'carga_remates.html', {'formulario':remate_formulario})

def cargar_lic(request):
    if request.method=='POST':
        form=licitacionForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            objeto=info['objeto']
            referencia=info['referencia']
            fecha=info['fecha']
            link=info['link']
            licitacion=Licitacion(objeto=objeto,referencia=referencia,fecha=fecha,link=link)
            licitacion.save()
            licitacion_formulario=licitacionForm()
            return render(request,'carga_licitaciones.html', {'mensaje':'Licitación cargada', 'formulario':licitacion_formulario})
        return render(request,'carga_licitaciones.html', {'mensaje':'Datos inválidos'})
    else:
        licitacion_formulario=licitacionForm()
        return render(request,'carga_licitaciones.html', {'formulario':licitacion_formulario})
    
def cargar_mart(request):
    if request.method=='POST':
        form=martilleroForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            apellido=info['apellido']
            matricula=info['matricula']
            email=info['email']
            martillero=Martillero(nombre=nombre,apellido=apellido,matricula=matricula,email=email)
            martillero.save()
            martillero_formulario=martilleroForm()
            return render(request,'carga_martilleros.html', {'mensaje':'Martillero cargado', 'formulario':martillero_formulario})
        return render(request,'carga_martilleros.html', {'mensaje':'Datos inválidos'})
    else:
        martillero_formulario=martilleroForm()
        return render(request,'carga_martilleros.html', {'formulario':martillero_formulario})

def cargar_clie(request):
    if request.method=='POST':
        form=clienteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            apellido=info['apellido']
            numero_de_cliente=info['numero_de_cliente']
            email=info['email']
            cliente=Cliente(nombre=nombre,apellido=apellido,numero_de_cliente=numero_de_cliente,email=email)
            cliente.save()
            cliente_formulario=clienteForm()
            return render(request,'carga_clientes.html', {'mensaje':'Cliente cargado', 'formulario':cliente_formulario})
        return render(request,'carga_clientes.html', {'mensaje':'Datos inválidos'})
    else:
        cliente_formulario=clienteForm()
        return render(request,'carga_clientes.html', {'formulario':cliente_formulario})
    
def cargar_opera(request):
    if request.method=='POST':
        form=operadorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            apellido=info['apellido']
            email=info['email']
            operador=Operador(nombre=nombre,apellido=apellido,email=email)
            operador.save()
            operador_formulario=operadorForm()
            return render(request,'carga_operadores.html', {'mensaje':'Operador cargado', 'formulario':operador_formulario})
        return render(request,'carga_operadores.html', {'mensaje':'Datos inválidos'})
    else:
        operador_formulario=operadorForm()
        return render(request,'carga_operadores.html', {'formulario':operador_formulario})  

# Vista de búsquedas y resultados

# Remates

def busquedaRemate(request):
    return render(request,'busqueda_remates.html')

def busquedaBien(request):
    bien=request.GET['bien']
    if bien!='':
        remates=Remate.objects.filter(bien__icontains=bien)
        return render(request,'resultados_remates.html', {'remates':remates})
    else:
        return render(request,'busqueda_remates.html', {'mensaje':'Por favor, ingresá algún término de búsqueda'})

# Licitaciones 

def busquedaLicitacion(request):
    return render(request,'busqueda_licitaciones.html')

def busquedaObjeto(request):
    objeto=request.GET['objeto']
    if objeto!='':
        licitaciones=Licitacion.objects.filter(objeto__icontains=objeto)
        return render(request,'resultados_licitaciones.html', {'licitaciones':licitaciones})
    else:
        return render(request,'busqueda_licitaciones.html', {'mensaje':'Por favor, ingresá algún término de búsqueda'})
    
# Licitaciones 

def busquedaCliente(request):
    return render(request,'busqueda_clientes.html')

def busquedaNumero(request):
    numero_de_cliente=request.GET['numero_de_cliente']
    if numero_de_cliente!='':
        clientes=Cliente.objects.filter(numero_de_cliente__icontains=numero_de_cliente)
        return render(request,'resultados_clientes.html', {'clientes':clientes})
    else:
        return render(request,'busqueda_clientes.html', {'mensaje':'Por favor, ingresá algún término de búsqueda'})
