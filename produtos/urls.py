from django.urls import path, include
from . import views

urlpatterns = [
    path('produtos/' , views.produtos, name="produtos"),
    path('clientes/', include('clientes.urls')),
    path('enderecos/' , include('enderecos.urls'))
]