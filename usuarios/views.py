from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm

class RegistroUsuarioView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("usuarios:login")
    template_name = "usuarios/registro.html"