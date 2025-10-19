from django.urls import path
from . import views

urlpatterns = [
    path('produtos/' , views.cadastro_produtos, name="cadastro_produtos")
]