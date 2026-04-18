import uuid
from django.db import models
from usuarios.models import Integrantes
from hierarquia.models import Graduacao


class Certificado(models.Model):
    # Identificador único para autenticação no site de cada certificado
    chave_autenticacao = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    integrante = models.ForeignKey(
        Integrantes, on_delete=models.CASCADE, related_name='certificados')
    graduacao_alcancada = models.ForeignKey(
        Graduacao, on_delete=models.PROTECT)
    data_emissao = models.DateField(auto_now_add=True)

    # Campo para o arquivo do certificado (PDF, imagem, etc.)
    arquivo = models.FileField(
        upload_to='certificados/arquivos/', null=True, blank=True)

    foi_impresso_fisicamente = models.BooleanField(
        default=False, verbose_name='Certificado impresso?')
    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'

    def __str__(self):
        return (
            f"Certificado de {self.graduacao_alcancada.nome} - "
            f"{self.integrante.get_full_name()}"
        )
