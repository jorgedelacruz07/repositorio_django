from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.utils import timezone
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User
from .models import*
from django.utils import timezone
@login_required
def subir_archivos(request):
	
	form = DocumentoA(request.POST,request.FILES)
	titulo=""
	context={"form":form,
			  "titulo":titulo}

	if form.is_valid():
		instance = form.save(commit=False)
		
		instance.user = request.user
		instance.save()
		form.save()
		form = DocumentoA()
		context={
			"titulo":"El archivo se subio correctamente",
			"form":form
		}

	
	return render(request,'Documentos/subir_archivos.html',context)


def comentario(request):
	
	form= ComentarioC()
	context={'form':form}
		

	return render(request,'Documentos/comentario.html',context)


@login_required
def archivos_list(request):
	return render_to_response("Documentos/archivo_list.html",{ 'user': request.user })

@login_required
def archivos_reciente(request):
	
	today = timezone.now().date()
	queryset_list = Archivo.objects.all().order_by("-timestamp")
	
	
	query = request.GET.get("q")
	print(query)
	if query:
		queryset_list = queryset_list.filter(
				Q(nombre__icontains=query)|
				Q(user__first_name__icontains=query)
				).distinct()
	
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset, 
		"title": "Archivos Subidos",
		"page_request_var": page_request_var,
		"today": today,
		
	}
	
	return render(request, "Documentos/archivo_reciente.html", context)
@login_required
def verprofesor(request):
	id_profe=request.GET.get('id')
	profesor=Profesor.objects.get(id=id_profe)
	
	context={'user':request.user, 'profesor':profesor}	
	return render(request,"Profesores/verprofesor.html",context)


def mostrarprofesores(request):
	profesores=Profesor.objects.all()
	form= ComentarioC(request.POST)
	if form.is_valid():
		comentario=form.save(commit=False)
		comentario.user=request.user
		comentario.save()
		form.save()
	return render(request,'Profesores/mostrarprofesor.html',{'profesores':profesores})


def mostrararea(request):
	areas=Area.objects.all()
	context={
		"areas":areas,
	}
	return render_to_response('Mostrar/mostrararea.html',context)

def mostrarprofesor(request):
	profesores=Profesor.objects.all()
	context={
		"profesores":profesores,
	}
	return render_to_response('Mostrar/mostrarprofesor.html',context)
def mostrarcurso(request):
	cursos=curso.objects.all()
	context={
		"cursos":cursos,
	}
	return render_to_response('Mostrar/mostrarcurso.html',context)	
