from django.contrib import admin
from .models import Evento, FotoEvento, Aviso


class FotoEventoInline(admin.TabularInline):
    model = FotoEvento
    extra = 1


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'local', 'publicado', 'fechado')
    list_filter = ('publicado', 'fechado', 'data_evento')
    inlines = [FotoEventoInline]


@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado', 'data_postagem')
    list_filter = ('publicado', 'data_postagem', 'autor')
    search_fields = ('titulo', 'texto')
