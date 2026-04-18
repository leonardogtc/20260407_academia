from django.db import models


class Modalidade(models.Model):
    nome = models.CharField(max_length=100)     # Ex: Capoeira, Karatê
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Graduacao(models.Model):
    modalidade = models.ForeignKey(
        # Ex: Professor, Mestre, Corda Azul, Faixa Preta
        Modalidade, on_delete=models.CASCADE, related_name='graduacoes'
    )
    nome = models.CharField(max_length=100)
    ordem = models.PositiveIntegerField(
        help_text="Quanto maior, mais graduado")
    pode_ter_alunos = models.BooleanField(default=False)
    valor_graduacao = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00,
        help_text="Valor para obter esta graduação"
    )

    class Meta:
        ordering = ['-ordem']  # Graduados mais altos primeiro
        verbose_name_plural = "Graduações"

    def __str__(self):
        return f"{self.nome} ({self.modalidade})"

