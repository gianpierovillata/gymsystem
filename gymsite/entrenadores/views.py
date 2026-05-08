from django.shortcuts import render
from .models import Entrenador

# Create your views here.

def index(request):
    entrenadores = Entrenador.objects.all()
    return render(request, 'entrenadores.html', {'entrenadores': entrenadores})
