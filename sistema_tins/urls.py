
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Comando para criação de admin: 
    # python manage.py createsuperuser
    # admin criado Nome: root ; Senha: root
    path('admin/', admin.site.urls), 
    path('clientes/' , include('clientes.urls'))
]
