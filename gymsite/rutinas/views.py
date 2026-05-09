from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Rutina


# Create your views here.
def index(request):
    rutinas = Rutina.objects.select_related('usuario').prefetch_related('ejercicios__ejercicio')
    template = loader.get_template('rutinas.html')    
    return HttpResponse(template.render({'rutinas': rutinas}))