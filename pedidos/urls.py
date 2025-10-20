from django.urls import path, include
from . import views

urlpatterns = [
    path('' , views.index_pedidos, name="index_pedidos"),
    path('criar_pedido' , views.criar_pedido, name="criar_pedido"),
    path('clientes/' , include('clientes.urls'), name='clientes'),
    path('produtos/' , include('produtos.urls'), name='produtos'),
    path('enderecos/' , include('enderecos.urls'), name='enderecos'),
    path('deletar_pedido/<int:id>' , views.deletar_pedidos, name="deletar_pedidos")
]