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
		nombre=form.cleaned_data.get("nombre")
		instance.user = request.user
		instance.save()
		form.save()
		form = DocumentoA()
		context={
			"titulo":"El archivo se subio correctamente",
			"form":form
		}

	
	return render(request,'subir_archivos.html',context)
@login_required
def archivos_list(request):
	return render_to_response("archivo_list.html",{ 'user': request.user })

@login_required
def archivos_reciente(request):
	
	today = timezone.now().date()
	queryset_list = Archivo.objects.all()
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Archivo.objects.all().order_by("-timestamp")
	
	"""query = request.GET.get("q")
	print(query)
	if query:
		queryset_list = queryset_list.filter(
				Q(nombre__icontains=query)|
				Q(archivo__icontains=query)|
				Q(user__first_name__icontains=query)|
				Q(user__last_name__icontains=query)
				).distinct()
	"""
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
	
	return render(request, "archivo_reciente.html", context)

def get_curso(request):
    id_area = request.GET['area_id']
    
    cursos = curso.objects.none()
    options = '<option value="" selected="selected">---------</option>'

    if id_area:
        cursos = curso.objects.filter(area=id_area) 
        
    for curs in cursos:
        
        options += '<option value="%s">%s</option>' % (
            curs.id,
            curs.curso
        )
    response = {}
    response['cursos'] = options
    print (options)
    return JsonResponse(response)


def get_profesor(request):
    curso_id = request.GET['curso_id']
    profesores = Profesor.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if curso_id:
        profesores = Profesor.objects.filter(curso=curso_id)   
    for profe in profesores:
        options += '<option value="%s">%s</option>' % (
            profe.id,
            profe.nombre
        )
    response = {}
    response['profesores'] = options
    return JsonResponse(response)

def get_datos(request):
	id_profesor= request.GET['profesor_id']
	profesores=Profesor.objects.filter(id=id_profesor)
	data=""
	for pro in profesores:
			data+='<p>Nombre : %s </p> <p>Apellido : %s </p><p>Email : %s'%(pro.nombre,pro.apellido,pro.email) 
	response={}
	response['profesores']=data
	return JsonResponse(response)	
def get_votos(request):
	id_archivo=request.GET["archi_id"]
	archivo=Archivo.objects.get(id=id_archivo)
	archivo.votos=archivo.votos+1
	archivo.save()
	response={}
	response['votos']=archivo.votos

	return JsonResponse(response)
def get_votos_less(request):
	id_archivo=request.GET["archi_id"]
	archivo=Archivo.objects.get(id=id_archivo)
	archivo.votos=archivo.votos-1
	archivo.save()
	response={}
	response['votos']=archivo.votos

	return JsonResponse(response)
def mostrararea(request):
	areas=Area.objects.all()
	context={
		"areas":areas,
	}
	return render_to_response('mostrararea.html',context)

def mostrarprofesor(request):
	profesores=Profesor.objects.all()
	context={
		"profesores":profesores,
	}
	return render_to_response('mostrarprofesor.html',context)



def mostrarcurso(request):
	cursos=curso.objects.all()
	context={
		"cursos":cursos,
	}
	return render_to_response('mostrarcurso.html',context)	
def archivoxarea(request):
 	id_area=request.GET["id"]
 	archivos=Archivo.objects.filter(area=id_area)
 	data=""
 	for archi in archivos:
 		data+="<div class='panel panel-primary row'><div class='panel-heading'><p><strong>Autor:%s</strong></p></div><div class='panel-body'><div class='sub_left'><p><strong> Nombre Archivo:</strong><span> %s</span></p><p><strong> Area:</strong><span>%s</span></p><p><strong>Curso: </strong><span>%s</span></p><p> <strong>Profesor: </strong><span>%s</span></p><hr> <a href='/static/%s' class='btn ' role='button' target='_blank'>  Ver  </a></div></div></div></div>"%(archi.user.username,archi.nombre,archi.area,archi.curso,archi.profesor,archi.archivo)
 	response={}
 	response['archivos']=data
 	return JsonResponse(response)

def archivoxcurso(request):
	id_curso=request.GET["id"]
	archivos=Archivo.objects.filter(curso=id_curso)
	data=""
	for archi in archivos:
		data+="<div class='panel panel-primary row'><div class='panel-heading'><p><strong>Autor:%s</strong></p></div><div class='panel-body'><div class='sub_left'><p><strong> Nombre Archivo:</strong><span> %s</span></p><p><strong> Area:</strong><span>%s</span></p><p><strong>Curso: </strong><span>%s</span></p><p> <strong>Profesor: </strong><span>%s</span></p><hr> <a href='/static/%s' class='btn ' role='button' target='_blank'>  Ver  </a></div></div></div></div>"%(archi.user.username,archi.nombre,archi.area,archi.curso,archi.profesor,archi.archivo)
	response={}
    
	response['archivos']=data
	return JsonResponse(response)
def archivoxprofesor(request):
	id_profesor=request.GET["id"]
	archivos=Archivo.objects.filter(profesor=id_profesor)
	data=""
	for archi in archivos:
		data+="<div class='panel panel-primary row'><div class='panel-heading'><p><strong>Autor:%s</strong></p></div><div class='panel-body'><div class='sub_left'><p><strong> Nombre Archivo:</strong><span> %s</span></p><p><strong> Area:</strong><span>%s</span></p><p><strong>Curso: </strong><span>%s</span></p><p> <strong>Profesor: </strong><span>%s</span></p><hr> <a href='/static/%s' class='btn ' role='button' target='_blank'>  Ver  </a></div></div></div></div>"%(archi.user.username,archi.nombre,archi.area,archi.curso,archi.profesor,archi.archivo)
	response={}
    
	response['archivos']=data
	return JsonResponse(response)