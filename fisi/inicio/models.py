from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Alumno(models.Model):
	
	usuario=models.OneToOneField('auth.User')
	codigo=models.CharField(max_length=8, blank=False,null=False)
	telefono=models.CharField(max_length=9, blank=False,null=False)
	direccion= models.CharField(max_length=50, blank=False,null=False)
	media = models.FileField(upload_to='myfolder/', blank= True, null= True)
	distrito=models.ForeignKey('Distrito',on_delete=models.CASCADE,blank=False,null=True)
	eap=models.ForeignKey('EAP',on_delete=models.CASCADE,blank=False,null=True)
	plan=models.ForeignKey('plan_estudio',on_delete=models.CASCADE,blank=False,null=True)
	sexo=models.ForeignKey('Sexo',on_delete=models.CASCADE,blank=False,null=True)


	def __str__(self): #para python 3 es __str__
		return self.codigo

class Distrito(models.Model):

	nombre_distrito=models.CharField(max_length=30, blank=False,null=False)
	provincia=models.ForeignKey('Provincia',on_delete=models.CASCADE,blank=False,null=False)

	def __str__(self): #para python 3 es __str__
		return self.nombre_distrito

class Provincia(models.Model):
	nombre_provincia=models.CharField(max_length=30, blank=False,null=False)
	departamento=models.ForeignKey('Departamento', on_delete=models.CASCADE,blank=False,null=False)

	def __str__(self): #para python 3 es __str__
		return self.nombre_provincia

class Departamento(models.Model):
	nombre_departamento=models.CharField(max_length=30, blank=False,null=False)

	def __str__(self): #para python 3 es __str__
		return self.nombre_departamento

class EAP(models.Model):
	nombre_eap=models.CharField(max_length=30, blank=False,null=False)

	def __str__(self): #para python 3 es __str__
		return self.nombre_eap

class plan_estudio(models.Model):
	plan= models.CharField(max_length=10, blank=False, null=False)
	eap= models.ForeignKey('EAP',on_delete=models.CASCADE,blank=False,null=False)

	def __str__(self): #para python 3 es __str__
		return self.plan
class Sexo(models.Model):
	sex=models.CharField(max_length=10, blank=False, null=False)
	def __str__(self): #para python 3 es __str__
		return self.sex

