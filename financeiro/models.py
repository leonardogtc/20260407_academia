from django.db import models
from usuarios.models import Integrantes


class CategoriaDespesa(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Categoria de Despesa"
        verbose_name_plural = "Categorias das Despesas"

    def __str__(self):
        return self.nome


class Despesa(models.Model):
    categoria = models.ForeignKey(CategoriaDespesa, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=255)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    paga = models.BooleanField(default=False)
    data_pagamento = models.DateField(
        null=True, blank=True, verbose_name="Data do Pagamento")

    def __str__(self):
        return (
            f"{self.categoria.nome} - {self.descricao} "
            f"- R$ {self.valor_total} - {self.data_vencimento}"
        )


class PagamentoGraduacao(models.Model):
    aluno = models.ForeignKey(Integrantes, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(auto_now_add=True)
    confirmado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Pagamento de Graduação"
        verbose_name_plural = "Pagamentos das Graduações"

    def __str__(self):
        return f"Pagamento: {self.aluno.first_name} - R$ {self.valor}"
