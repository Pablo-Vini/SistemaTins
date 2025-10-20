from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pedido
from clientes.models import Cliente
from enderecos.models import Endereco
from produtos.models import Produto

def index_pedidos(request):
    if request.method == 'GET':
        pedidos = Pedido.objects.all()
        return render(request, 'index_pedidos.html', {'pedidos':pedidos})
    elif request.method == 'POST':
        codigo = request.POST.get('codigo')
        cliente = request.POST.get('cliente')
        produto = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')
        valor_total = request.POST.get('valor_total')
        endereco = request.POST.get('endereco')

        pedido = Pedido(codigo=codigo, cliente=cliente, produto=produto,quantidade=quantidade, valor_total=valor_total, endereco=endereco)
        pedido.save()
        return HttpResponse('Pedido realizado com sucesso!')

def clientes(request):
    return render(request, 'cadastro_cliente.html')

def produtos(request):
    return render(request, 'produtos.html')

def enderecos(request):
    return render(request, 'enderecos.html')

def deletar_pedidos(request, id):
    produto = Pedido.objects.get(id=id)
    produto.delete()

    return redirect('index_pedidos')

def criar_pedido(request):
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    enderecos = Endereco.objects.all()

    return render(request, 'criar_pedido.html', {'clientes':clientes, 'enderecos':enderecos, 'produtos':produtos})