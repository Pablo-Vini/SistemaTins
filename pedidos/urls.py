from django.urls import path
from . import views

urlpatterns = [
    path('index/' , views.index_pedidos, name="index_pedidos")
]