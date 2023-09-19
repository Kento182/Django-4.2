from django.shortcuts import render
from django.http import HttpResponse


def primera_vista(request):
    return HttpResponse("Hola Mundo, desde <b>El Curso de Django para profesionales</b>")