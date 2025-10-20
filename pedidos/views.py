from django.shortcuts import render

def index_pedidos(request):
    return render(request, 'index_pedidos.html')

def clientes(request):
    return render(request, 'cadastro_cliente.html')

def produtos(request):
    return render(request, 'produtos.html')

def enderecos(request):
    return render(request, 'enderecos.html')
