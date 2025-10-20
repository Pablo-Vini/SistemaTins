from django.contrib import admin
from .models import Endereco

#Permite adicionar dados no Banco pelo acesso de admin
admin.site.register(Endereco)
