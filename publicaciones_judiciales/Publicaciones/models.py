from django.db import models

# Create your models here.

# Creo la clase remate con algunos de los datos de un remate judicial
 
class Remate(models.Model):

    bien = models.CharField(max_length=90)
    base = models.IntegerField()
    fecha = models.DateField()
    lugar = models.CharField(max_length=50)

# La clase Licitaciones tiene campos de convocatoria
    
class Licitacion(models.Model):
    
    objeto = models.CharField(max_length=90)
    referencia = models.CharField(max_length=60)
    fecha = models.DateField()
    link = models.URLField()

# El cliente usuario de la app

class Cliente(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_de_cliente = models.IntegerField()
    email = models.EmailField()

# El dataentry que carga remates y licitaciones

class Operador(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

# Usuario de la app y puede cargar remates

class Martillero(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    matricula = models.IntegerField()