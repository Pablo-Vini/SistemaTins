from django.shortcuts import render

def index_pedidos(request):
    return render(request, 'index_pedidos.html')
