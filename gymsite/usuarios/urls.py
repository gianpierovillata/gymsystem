from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('listado/', views.listado_usuarios, name='listado_usuarios'),
]