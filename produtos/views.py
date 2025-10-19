from django.shortcuts import render

def produtos(request):
    return render(request, 'produtos.html')
