from django.db import models

class Pedido(models.Model):
    codigo = models.CharField(max_length=11)
    cliente = models.CharField(max_length=20)
    produto = models.CharField(max_length=50)
    quantidade = models.CharField(max_length=50)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    endereco = models.CharField(max_length=20)
    
    def __str__(self):
        return self.codigo