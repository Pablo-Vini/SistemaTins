from django.contrib import admin
from .models import Pedido

#Permite adicionar dados no Banco pelo acesso de admin
admin.site.register(Pedido)
