from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pedido, PedidoItem
from clientes.models import Cliente
from enderecos.models import Endereco
from produtos.models import Produto
import json
from decimal import Decimal
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.shortcuts import get_object_or_404

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

def novo_pedido(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return HttpResponseBadRequest('JSON inválido')

    cliente_id = data.get('cliente_id')
    cliente_cpf = data.get('cliente_cpf')
    endereco_id = data.get('endereco_id')
    produtos = data.get('produtos')

    if not cliente_id or not endereco_id or not produtos:
        return HttpResponseBadRequest('cliente_id, endereco_id e produtos são obrigatórios')

    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if cliente.cpf != str(cliente_cpf):
        return HttpResponseBadRequest('CPF do cliente não confere')

    endereco = get_object_or_404(Endereco, pk=endereco_id, cliente=cliente)

    pedido = Pedido.objects.create(cliente=cliente, endereco=endereco, total=0)
    total = Decimal('0.00')

    for item in produtos:
        produto_id = item.get('produto_id')
        quantidade = item.get('quantidade') or item.get('q') or 0
        valor_unitario = item.get('valor_unitario')
        if not produto_id or not quantidade or valor_unitario is None:
            pedido.delete()
            return HttpResponseBadRequest('cada produto precisa de produto_id, quantidade e valor_unitario')

        produto = get_object_or_404(Produto, pk=produto_id)
        valor = Decimal(str(valor_unitario))
        quantidade = int(quantidade)
        PedidoItem.objects.create(
            pedido=pedido,
            produto=produto,
            codigo=item.get('codigo', produto.codigo),
            quantidade=quantidade,
            valor_unitario=valor
        )
        total += valor * quantidade

    pedido.total = total
    pedido.save()

    return JsonResponse({'pedido_id': pedido.id})