
from django.urls import path

from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('listado/', views.listado_usuarios, name='listado_usuarios'),
]