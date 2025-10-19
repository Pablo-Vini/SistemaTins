from django.urls import path
from . import views

urlpatterns = [
    path('enderecos/' , views.enderecos, name="enderecos")
]