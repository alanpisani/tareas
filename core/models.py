from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.CharField(max_length = 100)
    completado = models.BooleanField()

    def __str__(self):
        return self.contenido