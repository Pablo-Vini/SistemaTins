from django.contrib import admin
from .models import Produto

#Permite adicionar dados no Banco pelo acesso de admin
admin.site.register(Produto)
