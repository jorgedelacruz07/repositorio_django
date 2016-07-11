from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone
from .validators import valid_extension
class Profesor(models.Model):
	nombre=models.CharField(max_length=50, blank=False,null=False)
	apellido=models.CharField(max_length=50, blank=False,null=False)
	email=models.EmailField(max_length=50, blank=False,null=False)
	curso=models.ForeignKey('curso',null=True)
	area=models.ForeignKey('Area', null=True)
	Comentario=models.ForeignKey('Comentario',null=True)
	def __str__(self):
		return self.nombre
class Area(models.Model):
	area=models.CharField(max_length=50, blank=False,null=False)
	def __str__(self):
		return self.area
class curso(models.Model):
	curso=models.CharField(max_length=50, blank=False,null=False)
	area=models.ForeignKey('Area',null=True)
	def __str__(self):
		return self.curso

class Archivo(models.Model):
	nombre=models.CharField(max_length=50, blank=False,null=False)
	archivo=models.FileField(upload_to='documentos/', blank= False, null= True,validators=[valid_extension])
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	votos=models.IntegerField(blank=True,null=True, default=0)
	tipo=models.ForeignKey('tipo_doc',null=True)
	area=models.ForeignKey('Area',null=True)
	curso =models.ForeignKey('curso',null=True)
	profesor=models.ForeignKey('Profesor',null=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False,null=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

	def __str__(self): #para python 3 es __str__
		return self.nombre

class tipo_doc(models.Model):
	tipo=models.CharField(max_length=30,blank=False, null=False)
	def __str__(self):
		return self.tipo


class votante(models.Model):
	usuario=models.CharField(max_length=50, blank=False,null=False)
	archivo=models.CharField(max_length=50, blank=False,null=False)
	def __str__(self):
		return self.archivo
class Comentario(models.Model):
	comentario=models.TextField(max_length=500,null=False, blank=False)
	Profesor=models.ForeignKey('Profesor',null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False,null=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
	def __str__(self):
		return self.comentario