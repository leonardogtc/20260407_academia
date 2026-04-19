from django.db import models
from django.core.exceptions import ValidationError
from usuarios.models import Integrantes


class Evento(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título do Evento')
    data_evento = models.DateField(verbose_name='Data do Evento')
    local = models.CharField(max_length=255, verbose_name='Local do Evento')
    descricao = models.TextField(verbose_name='Descrição do Evento')
    banner = models.ImageField(
        upload_to='eventos/banners/', null=True, blank=True)

    publicado = models.BooleanField(default=False, verbose_name='Publicado?')
    fechado = models.BooleanField(default=False, verbose_name='Fechado?')
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-data_evento']

    def __str__(self):
        return self.titulo

    def clean(self):
        # Lógica de "Velha Guarda": Proteção de dados históricos
        if self.pk:  # Se o objeto já existe no banco (é uma edição)
            obj_original = Evento.objects.get(pk=self.pk)
            if obj_original.fechado:
                raise ValidationError(
                    "Este evento está 'Fechado' e não pode mais ser alterado. "
                    "É um registro histórico."
                )

    class Aviso(models.Model):
        titulo = models.CharField(max_length=200)
        texto = models.TextField()
        autor = models.ForeignKey(
            Integrantes,
            on_delete=models.CASCADE,
            limit_choices_to={'is_staff': True}
        )

        permite_comentarios = models.BooleanField(default=False)
        publicado = models.BooleanField(default=True)

        data_postagem = models.DateTimeField(auto_now_add=True)

        class Meta:
            ordering = ['-data_postagem']

        def __str__(self):
            return self.titulo
