from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *

class HomeView(TemplateView):
    template_name = "bases/home.html"