from django.db import models
from django.contrib.auth.models import User
 

# Create your models here.

class Perfil(models.Model):
    descripcion = models.CharField(max_length=2200)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.usuario}"


class Publicacion(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=300)
    contenido = models.CharField(max_length=2200)
    fecha = models.DateField()    
    imagen = models.FileField(upload_to="media/posts", null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

#    epigrafe = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.titulo}"


class Opinion(models.Model):
    texto = models.CharField(max_length=2200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"@{self.autor}: '{self.publicacion}'"
    
    
class Avatar(models.Model):
    imagen = models.FileField(upload_to="media/avatares", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"