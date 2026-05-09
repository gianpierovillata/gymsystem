from django.contrib import admin
from .models import Rutina, ListaEjercicios


class ListaEjerciciosInline(admin.TabularInline):
    model = ListaEjercicios
    extra = 1


@admin.register(Rutina)
class RutinaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'objetivo', 'cliente')
    inlines = [ListaEjerciciosInline]