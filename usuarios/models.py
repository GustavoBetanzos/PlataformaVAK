from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):

    TIPO_VAK = [
        ('V', 'Visual'),
        ('A', 'Auditivo'),
        ('K', 'Kinestesico'),
    ]

    tipo_aprendizaje = models.CharField(
        max_length=1,
        choices=TIPO_VAK,
        null=True,
        blank=True
    )