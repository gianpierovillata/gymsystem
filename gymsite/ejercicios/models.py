from django.db import models
# Create your models here.

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    grupomuscular = models.CharField(max_length=100)
   

    def __str__(self):
        return f"{self.nombre} - {self.grupomuscular}"