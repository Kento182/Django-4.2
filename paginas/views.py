from django.shortcuts import render
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "paginas/about.html"
    
class ForbiddenView(TemplateView):
    template_name = "paginas/forbidden.html"