
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return HttpResponse("Bienvenidos usuarios")

def listado_usuarios(request):
    usuarios = ["Usuario 1", "Usuario 2", "Usuario 3"]
    return HttpResponse(f"Listado de usuarios: {', '.join(usuarios)}")