from django.contrib import admin
from .models import *

 
class AdminDocumento(admin.ModelAdmin):
	list_display=["user","nombre","archivo"] #la vista de la base de datos admin
	
# Register your models here.
admin.site.register(Archivo,AdminDocumento)
admin.site.register(curso)
admin.site.register(Area)
admin.site.register(Profesor)
admin.site.register(tipo_doc)
admin.site.register(Comentario)