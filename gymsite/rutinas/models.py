from django.db import models
from clientes.models import Cliente
from ejercicios.models import Ejercicio


# Create your models here.

   

class Rutina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    objetivo = models.CharField(max_length=100)   
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
 
  

class ListaEjercicios(models.Model):

    rutina = models.ForeignKey(
        Rutina, 
        on_delete=models.CASCADE,
        related_name='ejercicios'
    )


    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    series = models.IntegerField()
    repeticiones = models.IntegerField()   
    descanso = models.IntegerField()
    intensidad = models.IntegerField() 

    def __str__(self):
        return f"{self.rutina.nombre} - {self.ejercicio.nombre}"
   

    
