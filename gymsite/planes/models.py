from django.db import models
from rutinas.models import Rutina
from clientes.models import Cliente

# Create your models here.

class Planes(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.IntegerField()  # Duración en meses
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rutinas = models.ManyToManyField(Rutina, related_name='planes')

    def __str__(self):
        return self.nombre