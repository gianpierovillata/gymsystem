from django.db import models


# Create your models here.

class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)    
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    experiencia = models.IntegerField(blank=True, null=True)
    lugar_trabajo = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
