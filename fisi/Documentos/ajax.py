from django.contrib.auth.models import User
from .models import Area, Profesor, curso,Archivo,votante, Comentario
from django.http import JsonResponse

def vercomentarios(request):
    id_profe=request.GET['profesor_id']
    comentarios=Comentario.objects.filter(Profesor=id_profe)
    data=""
    for coment in comentarios:
        data+="<p>Usuario: %s</p> <p>Comentario: %s</p>"%(coment.user,coment.comentario)

    response={}
    response['comentarios']=data
    return JsonResponse(response)
       
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
    usern=request.user.username
    try:
        votn= votante.objects.filter(archivo=id_archivo).get(usuario=usern)
    except :
        voto= votante()
        voto.usuario=usern
        voto.archivo=id_archivo
        voto.save()
        archivo.votos=archivo.votos+1
        archivo.save()
        
    response={}
    response['votos']=archivo.votos
    
    return JsonResponse(response)

def get_votos_less(request):
	

    id_archivo=request.GET["archi_id"]
    archivo=Archivo.objects.get(id=id_archivo)
    usern=request.user.username
    try:
        votn= votante.objects.filter(archivo=id_archivo).get(usuario=usern)
    except :
        voto= votante()
        voto.usuario=usern
        voto.archivo=id_archivo
        voto.save()
        archivo.votos=archivo.votos-1
        archivo.save()
    response={}
    response['votos']=archivo.votos
    
    return JsonResponse(response)

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