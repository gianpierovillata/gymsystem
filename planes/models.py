from django.db import models
from rutinas.models import Rutinas


# Create your models here.

class Planes(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    dias = models.IntegerField()
    rutinas = models.ForeignKey(Rutinas, on_delete=models.CASCADE)
   