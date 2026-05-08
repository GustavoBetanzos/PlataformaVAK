from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from contenidos.models import Contenido

class Interaccion(models.Model):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)

    visto = models.BooleanField(default=False)
    calificacion = models.IntegerField(null=True, blank=True)

    fecha = models.DateTimeField(auto_now_add=True)