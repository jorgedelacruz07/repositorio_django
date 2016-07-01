from django.shortcuts import render

# Create your views here.
#views.py
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from .models import Alumno
from .forms import *

 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    #if request.user.is_superuser:
     #   raise Http404
    
    return render_to_response('home.html',{ 'user': request.user })
  

@login_required
def editar(request):

    form = EditarContrasenaForm(request.POST)
    context={
        "form":form,
        
    }
    if form.is_valid():
        request.user.password = make_password(form.cleaned_data['password'])
        request.user.save()
        context={
            "titulo":"La contraseña se cambio con exito",
            
        }
        return render(request, 'editar.html', context)
    else:
        form = EditarContrasenaForm()
    
    return render(request, 'editar.html', context)
