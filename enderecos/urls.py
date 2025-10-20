from django.urls import path
from . import views

urlpatterns = [
    path('enderecos/' , views.enderecos, name="enderecos"),
    path('ajax/cep/', views.ajax_cep, name="ajax_cep")
]