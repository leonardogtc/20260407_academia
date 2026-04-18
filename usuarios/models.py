from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from hierarquia.models import Graduacao


class Integrantes(AbstractUser):
    # O AbstractUser já tem: username, first_name, last_name, email, password,
    # is_staff, is_active, date_joined.
    # Campo para a hierarquia (Pai/Professor)
    # 'self' permite que um integrante aponte para outro integrante
    instrutor = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='alunos'
    )

    # Informações básicas que você solicitou
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)

    # Telefone e WhatsApp
    # Usaremos CharField porque telefones levam parênteses, traços e espaços
    telefone = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Telefone/WhatsApp')

    # Sobrescrevendo o e-mail para torná-lo obrigatório ou único, se desejar.
    email = models.EmailField(unique=True, null=False,
                              blank=False, verbose_name='E-mail Principal')

    # Status de vida do aluno
    STATUS_CHOICES = (
        ('A', 'Ativo'),
        ('I', 'Inativo'),
        ('F', 'Filiado Externo'),
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='A',
        verbose_name='Status'
    )

    # Relacionamento com a graduação
    graduacao = models.ForeignKey(
        Graduacao, null=True, blank=True, on_delete=models.PROTECT,
    )

    def clean(self):
        super().clean()

        # Só validamos se houver um instrutor e ambos tiverem graduação
        # definida
        if self.instrutor and self.graduacao and self.instrutor.graduacao:
            # Regra: A ordem do instrutor deve ser maior que a do aluno
            if self.instrutor.graduacao.ordem <= self.graduacao.ordem:
                raise ValidationError({
                    'instrutor': (
                        f"O instrutor {self.instrutor.get_full_name()} possui a graduação "
                        f"'{self.instrutor.graduacao.nome}' (Nível {self.instrutor.graduacao.ordem}), "
                        f"que não é superior à sua: '{self.graduacao.nome}' (Nível {self.graduacao.ordem})."
                    )
                })

    def save(self, *args, **kwargs):
        # Forçamos a validação antes de salvar no banco
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        # Uma boa prática da velha guarda: facilitar a identificação visual
        return f"{self.get_full_name()} - {self.username}"
