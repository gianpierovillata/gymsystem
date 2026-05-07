
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def bienvenida(request):
    template = loader.get_template('bienvenida.html')
    return HttpResponse(template.render())

def listado_usuarios(request):
    usuarios = ["Usuario 1", "Usuario 2", "Usuario 3"]
    return HttpResponse(f"Listado de usuarios: {', '.join(usuarios)}")