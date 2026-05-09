from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Planes

# Create your views here.

def index(request):
    template = loader.get_template('planes.html')
    planes = Planes.objects.all()
    return HttpResponse(template.render({'planes': planes}, request))