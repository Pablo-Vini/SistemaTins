from django.shortcuts import render
import requests
from django.http import JsonResponse
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

def ajax_cep(request):
    cep = request.GET.get("cep", "").strip().replace("-", "")
    if not (cep.isdigit() and len(cep) == 8):
        return JsonResponse({"erro": "CEP inválido"}, status=400)
    r = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)
    data = r.json()
    if data.get("erro"):
        return JsonResponse({"erro": "CEP não encontrado"}, status=404)
    return JsonResponse({
        "logradouro": data.get("logradouro", ""),
        "complemento": data.get("complemento", ""),
        "bairro": data.get("bairro", ""),
        "localidade": data.get("localidade", ""),
        "uf": data.get("uf", "")
    })