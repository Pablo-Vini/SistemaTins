from django.urls import path, include
from . import views

urlpatterns = [
    path('enderecos/' , views.enderecos, name="enderecos"),
    path('ajax/cep/', views.ajax_cep, name="ajax_cep")
]