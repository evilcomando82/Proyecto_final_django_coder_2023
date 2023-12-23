
from django.urls import path
from . import views
#from django.contrib.auth.views import LogoutView
from AppCoder.views import (
    PublicacionListView,
    PublicacionUpdateView,
    PublicacionDeleteView, 
    PublicacionCreateView,
    PublicacionDetailView,
    PublicacionListView2,
      
    )



urlpatterns = [
   
   
    
    #path("inicio/", views.inicio_view, name="inicio"),
    
    #path("loguear/", views.loguear_view, name="loguear"),

    path("loguear/", views.loguear_view, name="loguear"),

   # path('logout/', LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    path("registrar/", views.registro_view, name="registrar"),
    path('logout', views.logout_view, name="logout"),
   # path("crear-avatar", views.crear_avatar_view, name="crear-avatar"),
    path("profile/<user_id>", views.mostrar_profile_view, name="profile"),
    path("about/", views.about_view, name="about"),

    path("publicaciones_list/", PublicacionListView.as_view(), name="publicaciones_list"),
    path("publicaciones_update/<pk>", PublicacionUpdateView.as_view(), name="publicaciones_update"),
    path("publicaciones_delete/<pk>", PublicacionDeleteView.as_view(), name="publicaciones_delete"),
    path("publicaciones_create", PublicacionCreateView.as_view(), name="publicaciones_create"),
    path("publicaciones_detail/<pk>", PublicacionDetailView.as_view(), name="publicaciones_detail"),
    path("inicio/", PublicacionListView2.as_view(), name="inicio"),

    path("editar_perfil", views.editar_perfil_view, name="editar_perfil"),     

    path("publicaciones_busqueda/", views.publicacion_buscar_view, name="publicaciones_busqueda"),

]



from django.conf.urls.static import static
from django.conf import settings


url_patterns_for_media =static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + url_patterns_for_media