from django.http import HttpResponse
from django.template import loader
from .models import Ejercicio
# Create your views here.


def index(request):
    ejercicios = Ejercicio.objects.all().values()
    template =loader.get_template('ejercicios.html')    
    return HttpResponse(template.render({'ejercicios': ejercicios}))