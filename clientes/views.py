from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
from datetime import date

def ver_clientes(request):
    print(request)
    return HttpResponse('Olá tudo bem')

def cadastro_cliente(request):
    if request.method == "GET":
        return render(request, 'cadastro_cliente.html', {'nome': 'caio'})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        
        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            return HttpResponse('Usuário já está cadastrado!')
        else:
            data = date.today()
            data_cadastro = data.strftime("%d/%m/%Y")
            dados_cliente = Cliente(nome=nome, cpf=cpf, email=email, telefone=telefone, data_cadastro=data_cadastro)
            dados_cliente.save()
            return HttpResponse('Cadastro realizado com sucesso!')
         
        