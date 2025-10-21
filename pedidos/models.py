from django.db import models
from produtos.models import Produto

class Pedido(models.Model):
    codigo = models.CharField(max_length=11)
    cliente = models.CharField(max_length=20)
    produto = models.CharField(max_length=50)
    quantidade = models.CharField(max_length=50)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    endereco = models.CharField(max_length=20)
    
    def __str__(self):
        return self.codigo

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    codigo = models.CharField(max_length=50)
    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def line_total(self):
        return self.quantidade * self.valor_unitario