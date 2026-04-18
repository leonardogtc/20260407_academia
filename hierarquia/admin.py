from django.contrib import admin
from .models import Modalidade, Graduacao


@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Graduacao)
class GraduacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modalidade', 'ordem',
                    'pode_ter_alunos', 'valor_graduacao')
    list_filter = ('modalidade', 'pode_ter_alunos')
    search_fields = ('nome',)
