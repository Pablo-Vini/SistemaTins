from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    email = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
    
# Para criar a tabela e os campos no Banco de Dados, executar os seguintes comendos no terminal em sequência:
# >>python manage.py makemigrations
# >>python manage.py migrate