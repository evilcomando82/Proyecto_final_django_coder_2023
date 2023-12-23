from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Perfil)
admin.site.register(models.Avatar)
admin.site.register(models.Publicacion)
admin.site.register(models.Opinion)