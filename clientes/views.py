from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
from datetime import date

def ver_clientes(request):
    print(request)
    return HttpResponse('Olá tudo bem')

def cadastro_cliente(request):
    if request.method == "GET":
        return render(request, 'cadastro_cliente.html')
    elif request.method == "POST":
        hoje = date.today()

        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_cadastro = request.POST.get('data_cadastro')

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            return HttpResponse('Usuário já está cadastrado!')
        else:
            dados_cliente = Cliente(nome=nome, cpf=cpf, email=email, telefone=telefone, data_cadastro=data_cadastro)
            dados_cliente.save()
            return HttpResponse('Cadastro realizado com sucesso!')
         
        