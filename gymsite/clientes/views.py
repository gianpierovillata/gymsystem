from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

from django.template import loader
# Create your views here.

def index(request):
    clientes = Cliente.objects.all().values('nombre', 'apellido', 'telefono', 'fecha_nacimiento', 'edad', 'peso', 'altura')
    template = loader.get_template('clientes.html')
    return HttpResponse(template.render({'clientes': clientes}))  