"""fisi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from inicio.views import *
from Documentos.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^home/$', home),
    url(r'^editar/$', editar),
    url(r'^subir_archivos/$', subir_archivos),
    url(r'^archivos_reciente/$', archivos_reciente),
    url(r'^archivos_list/$', archivos_list),
    url(r'^getcurso/$', get_curso),
    url(r'^getprofesor/$', get_profesor),
    url(r'^getdatos/$', get_datos),
    url(r'^getvotos/$', get_votos),
    url(r'^getvotosless/$', get_votos_less),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^mostrararea/$', mostrararea ),
    url(r'^mostrarcurso/$', mostrarcurso ),
     url(r'^mostrarprofesor/$', mostrarprofesor ),
    url(r'^archivoxarea/$', archivoxarea),
    url(r'^archivoxcurso/$', archivoxcurso),
    url(r'^archivoxprofesor/$', archivoxprofesor),
    
    
]