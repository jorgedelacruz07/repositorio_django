from django.conf.urls import url, include, patterns
from Documentos.views import *
from Documentos.ajax import *

urlpatterns = [
    url(r'^subir_archivos/$', subir_archivos),
    url(r'^archivos_reciente/$', archivos_reciente),
    url(r'^archivos_list/$', archivos_list),
    url(r'^getcurso/$', get_curso),
    url(r'^getprofesor/$', get_profesor),
    url(r'^getdatos/$', get_datos),
    url(r'^getvotos/$', get_votos),
    url(r'^getvotosless/$', get_votos_less),
	url(r'^mostrararea/$', mostrararea ),
    url(r'^mostrarcurso/$', mostrarcurso ),
    url(r'^mostrarprofesor/$', mostrarprofesor ),
    url(r'^archivoxarea/$', archivoxarea),
    url(r'^archivoxcurso/$', archivoxcurso),
    url(r'^archivoxprofesor/$', archivoxprofesor),

]


