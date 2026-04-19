from django.contrib import admin
from .models import CategoriaDespesa, Despesa, PagamentoGraduacao


@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'descricao', 'valor_total',
                    'data_vencimento', 'paga')
    list_filter = ('paga', 'data_vencimento', 'categoria')
    list_editable = ('paga',)
    search_fields = ('descricao',)


@admin.register(PagamentoGraduacao)
class PagamentoGraduacaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'valor', 'data_pagamento', 'confirmado')
    list_filter = ('confirmado',)
    search_fields = ('aluno__first_name', 'aluno__username')


admin.site.register(CategoriaDespesa)
