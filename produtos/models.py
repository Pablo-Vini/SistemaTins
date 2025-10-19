from django.db import models

class Produto(models.Model):
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=200)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    data_cadastro = models.CharField(max_length=20)

    def __str__(self):
        return self.nome