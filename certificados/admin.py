from django.contrib import admin
from .models import Certificado


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    # Exibimos a chave de autenticação na lista para fácil consulta
    list_display = ('chave_autenticacao', 'integrante',
                    'graduacao_alcancada', 'data_emissao',
                    'foi_impresso_fisicamente')
    list_filter = ('graduacao_alcancada', 'foi_impresso_fisicamente')
    search_fields = ('integrante__first_name', 'chave_autenticacao')

    # A chave é gerada automaticamente, então não a exibimos no formulário
    # de edição
    readonly_fields = ('chave_autenticacao', 'data_emissao')
