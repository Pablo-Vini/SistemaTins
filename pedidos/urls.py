from django.urls import path, include
from . import views

urlpatterns = [
    path('' , views.index_pedidos, name="index_pedidos"),
    path('clientes/' , include('clientes.urls'), name='clientes'),
    path('produtos/' , include('produtos.urls'), name='produtos'),
    path('enderecos/' , include('enderecos.urls'), name='enderecos')
]