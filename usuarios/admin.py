from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Integrantes


@admin.register(Integrantes)
class IntegrantesAdmin(UserAdmin):
    # Adicionar novos campos personalizados nsa telas de edição do admin
    fieldsets = UserAdmin.fieldsets + (
        ('Informações do Grupo', {
            'fields': (
                'graduacao', 'instrutor', 'status'
            )
        }),
        ('Contato Pessoal', {
            'fields': (
                'data_nascimento', 'cpf', 'telefone'
            )
        })
    )

    list_display = ('username', 'get_full_name',
                    'graduacao', 'instrutor', 'status')
    list_filter = ('graduacao', 'status')


# Register your models here.
