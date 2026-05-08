from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Contenido(models.Model):

    TIPO = [
        ('video', 'Video'),
        ('texto', 'Texto'),
        ('imagen', 'Imagen'),
    ]

    VAK = [
        ('V', 'Visual'),
        ('A', 'Auditivo'),
        ('K', 'Kinestesico'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    tipo = models.CharField(max_length=10, choices=TIPO)
    estilo_vak = models.CharField(max_length=1, choices=VAK)

    archivo = models.FileField(upload_to='contenidos/')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    fecha_creacion = models.DateTimeField(auto_now_add=True)