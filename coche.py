from django.db import models

class Marca(models.Model):
	nombreMarca = models.CharField

class Modelo(models.Model):
	nombreModelo = models.CharField
	
class Coche(Marca, Modelo):
	fechaCreacion = models.DateTimeField(auto_now_add=True)