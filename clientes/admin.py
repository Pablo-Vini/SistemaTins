from django.contrib import admin
from .models import Cliente

#Permite adicionar dados no Banco pelo acesso de admin
admin.site.register(Cliente)
