from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
from datetime import date

def produtos(request):
    if request.method == "GET":
        return render(request, 'produtos.html')
    elif request.method == "POST":
        codigo = request.POST.get('codigo')
        descricao = request.POST.get('descricao')
        valor_unitario = request.POST.get('valor_unitario')

        produto = Produto.objects.filter(codigo=codigo)

        if produto.exists():
            return HttpResponse('Usuário já está cadastrado!')
        else:
            data = date.today()
            data_cadastro = data.strftime("%d/%m/%Y")
            dados_produto = Produto(codigo=codigo, descricao=descricao, valor_unitario=valor_unitario, data_cadastro=data_cadastro)
            dados_produto.save()
            return HttpResponse('Cadastro realizado com sucesso!')

def index_pedidos(request):
    return render(request, 'index_pedidos.html')

def clientes(request):
    return render(request, 'cadastro_cliente.html')

def enderecos(request):
    return render(request, 'enderecos.html')