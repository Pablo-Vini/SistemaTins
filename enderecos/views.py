from django.shortcuts import render


def enderecos(request):
    return render(request, 'enderecos.html')
