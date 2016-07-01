from django import forms
from .models import Archivo, Comentario

class DocumentoA(forms.ModelForm):

	class Meta: #pra el adminnistrador visual
		model=Archivo
		fields=["nombre","tipo","area","curso","profesor","archivo"]
		
class ComentarioC(forms.ModelForm):
	class Meta:
		model=Comentario
		fields=["comentario"]