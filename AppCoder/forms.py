
from django.contrib.auth.forms import UserCreationForm, UserModel
from django import forms
from .models import Opinion

class CrearUsuarioFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["password1", "password2", "username", "email"]
        help_texts = {k: "" for k in fields}

class OpinionForm (forms.ModelForm):
    texto = forms.Textarea()

    class Meta:
        model= Opinion
        fields =['texto'] 
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 5, 'cols': 180, 'placeholder': 'Escribe tu comentario aquí'}),
        }

class UserEditionFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = UserModel
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}

class PublicacionBuscarFormulario(forms.Form):
    publicacion = forms.CharField()
