from django.urls import path, include
from . import views

urlpatterns = [
    path('clientes_ver/' , views.ver_clientes, name="ver_clientes"),
    path('cadastro_cliente/' , views.cadastro_cliente, name="cadastro_cliente")
]