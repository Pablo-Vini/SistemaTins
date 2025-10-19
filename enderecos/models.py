from django.db import models

class Endereco(models.Model):
    titulo = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100)
    cliente = models.CharField(max_length=14)
    padrao = models.BooleanField()
    
    def __str__(self):
        return self.nome
