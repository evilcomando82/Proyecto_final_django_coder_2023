
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CrearUsuarioFormulario, OpinionForm, UserEditionFormulario, PublicacionBuscarFormulario
from django.contrib.auth.models import User
from .models import Publicacion, Perfil, Avatar
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
 

def inicio_view(request):
    if request.user.is_authenticated:
        usuario = request.user
        avatar = Avatar.objects.filter(user=usuario).first()
        avatar_url = avatar.imagen.url if avatar is not None else ""
        
    else:
        avatar_url = ""
    
        return render(request, "AppCoder/inicio.html", context={"avatar_url": avatar_url})




def about_view(request):
    if request.user.is_authenticated:
        usuario = request.user
        avatar = Avatar.objects.filter(user=usuario).first()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""
    return render(request, "AppCoder/about.html", context={"avatar_url": avatar_url})

def loguear_view(request):
    if request.user.is_authenticated:
        return render(
            request,
            "AppCoder/inicio.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            "AppCoder/loguear.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": f"Bienvenido {modelo.username}"} # type: ignore
            )
        else:
            return render(
                request,
                "AppCoder/loguear.html",
                {"form": formulario}
            )



def registro_view(request):

    if request.method == "GET":
        return render(
            request,
            "AppCoder/registrar.html",
            {"form": CrearUsuarioFormulario()}
        )
    else:
        formulario = CrearUsuarioFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": f"Usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "AppCoder/registrar.html",
                {"form": formulario}
            )

def logout_view(request):
    logout(request)
    mensaje = "ha salido del sistema"
    return render(request,"AppCoder/logout.html",{"mensaje": mensaje  })


def mostrar_profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    todos_los_posts = Publicacion.objects.filter(autor=user).all()
    perfil = Perfil.objects.filter(usuario=user).first()
    avatar = Avatar.objects.filter(user=user).first()
    avatar_url = avatar.imagen.url if avatar is not None else ""
    contexto = {"publicacion": todos_los_posts, "perfil": perfil, "avatar_url": avatar_url}

    return render(request, "AppCoder/instagram_profile.html", context=contexto)

####################  CRUD  Vistas basadas en Clases #########################################

from django.views.generic import ListView, CreateView, DeleteView, UpdateView

class PublicacionListView(LoginRequiredMixin, ListView):
    model = Publicacion
    context_object_name = "publicaciones"
    template_name = "AppCoder/publicaciones_list.html"

 #LoginRequiredMixin,
class PublicacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Publicacion
    template_name = "AppCoder/publicaciones_update.html"
    success_url = reverse_lazy("publicaciones_list")
    fields = ["titulo", "subtitulo", "contenido", "fecha", "imagen", "autor"]
    


class PublicacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = "AppCoder/publicaciones_delete.html"
    success_url = reverse_lazy("publicaciones_list")


class PublicacionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Publicacion
    template_name = "AppCoder/publicaciones_create.html"
    success_url = reverse_lazy("publicaciones_list")
    fields = ["titulo", "subtitulo", "contenido", "fecha", "imagen", "autor"]
    success_message = "publicacion creada con éxito!  :)" 
    widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', "class":"form-control"}),
        }
    
class PublicacionDetailView(generic.DetailView):
    model = Publicacion
    queryset = Publicacion.objects.all()
    template_name = "AppCoder/publicaciones_detail.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OpinionForm()
        return context

     
    def post(self, request, *args, **kwargs):
        publicacion = self.get_object()
        form = OpinionForm(request.POST)

        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.autor = request.user
            opinion.publicacion = publicacion
            opinion.save()
             
            return HttpResponseRedirect(reverse('publicaciones_detail', kwargs={'pk': publicacion.pk}))
        else:
              (request, 'Hubo un error al agregar el comentario. Por favor, verifica el formulario.')
              context = self.get_context_data()
        return self.render_to_response(context)

  
class PublicacionListView2(ListView):
    model = Publicacion
    context_object_name = "publicaciones2"
    template_name = "AppCoder/inicio.html"

  
 
@login_required
def editar_perfil_view(request):
    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).first()
    avatar_url = avatar.imagen.url if avatar is not None else ""

    if request.method == "POST":
        formulario = UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.email = informacion["email"]
            usuario.set_password(informacion["password1"])
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
            return redirect("inicio")
    else:
        valores_iniciales = {
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }
        formulario = UserEditionFormulario(initial=valores_iniciales)

    return render(request, "AppCoder/editar_perfil.html", context={"form": formulario, "usuario": usuario, "avatar_url": avatar_url})





def publicacion_buscar_view(request):
    if request.method == "GET":
        form = PublicacionBuscarFormulario()
        return render(
            request,
            "AppCoder/publicaciones_busqueda.html",
            context={"form": form}
        )
    else:
        formulario = PublicacionBuscarFormulario(request.POST)
        print(formulario.is_valid())
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            # Filtrar las publicaciones
            publicaciones_filtradas = Publicacion.objects.filter(titulo__icontains=informacion["publicacion"])

            contexto = {"publicaciones": publicaciones_filtradas}
            return render(request, "AppCoder/publicaciones_list.html", contexto)
        
