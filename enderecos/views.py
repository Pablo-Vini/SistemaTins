from django.shortcuts import render
from django.http import HttpResponse
from .models import Endereco

def enderecos(request):
    if request.method == "GET":
        return render(request, 'enderecos.html')
    elif request.method == "POST":
        titulo = request.POST.get('titulo')
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        cliente = request.POST.get('cliente')
        #padrao = request.POST.get('padrao')

        
        endereco = Endereco.objects.filter(cep=cep)

        if endereco.exists():
            return HttpResponse('Endereço já está cadastrado!')
        else:
            dados_endereco = Endereco(titulo=titulo, cep=cep, logradouro=logradouro, bairro=bairro, cidade=cidade, estado=estado, numero=numero, complemento=complemento, cliente=cliente, padrao=True)
            dados_endereco.save()
            return HttpResponse('Cadastro realizado com sucesso!')
