
from django.http import HttpResponse
from django.template import loader
from .models import Usuario
# Create your views here.


def index(request):
    usuarios = Usuario.objects.all()
    template = loader.get_template('usuarios.html')
    return HttpResponse(template.render({'usuarios': usuarios}))

