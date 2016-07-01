from django.contrib import admin
from .models import *

# Register your models here.
class AdminAlumno(admin.ModelAdmin):
	list_display=["codigo","telefono","direccion","media"] #la vista de la base de datos admin
	
class AdminProvincia(admin.ModelAdmin):
	list_display=["nombre_provincia","departamento"]
admin.site.register(Alumno, AdminAlumno)
admin.site.register(Distrito)
admin.site.register(Departamento)
admin.site.register(Provincia,AdminProvincia)
admin.site.register(EAP)
admin.site.register(plan_estudio)
admin.site.register(Sexo)