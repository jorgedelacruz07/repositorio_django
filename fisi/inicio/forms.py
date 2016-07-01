
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Alumno
 
    

class EditarEmailForm(forms.Form):
    email = forms.EmailField(
    widget=forms.EmailInput(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
   
        self.request = kwargs.pop('request')
        return super().__init__(*args, **kwargs)
    def clean_email(self):
        email = self.cleaned_data['email']
        # Comprobar si ha cambiado el email
        actual_email = self.request.user.email
        username = self.request.user.username
        if email != actual_email:
            # Si lo ha cambiado, comprobar que no exista en la db.
            # Exluye el usuario actual.
            existe = User.objects.filter(email=email).exclude(username=username)
            if existe:
                raise forms.ValidationError('Ya existe un email igual en la db.')
        return email
class EditarContrasenaForm(forms.Form):
    actual_password = forms.CharField(label='Contraseña actual',min_length=5,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Nueva contraseña',min_length=5,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repetir contraseña',min_length=5,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    def clean_password2(self):
    
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2