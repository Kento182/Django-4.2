from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class MarkList(ListView):
    template_name="ctrl_comb/mark.html"
    model=Mark
    context_object_name="obj"
    ordering=["decript"]
    

def mark_save(request):
    context = {}
    template_name = "ctrl_comb/mark-list.html"
    
    if request.method == "POST":
        i = request.POST.get("id")
        d = request.POST.get("decript")
        
        o = Mark.objects.create(decript = d)
    obj = Mark.objects.all().order_by("decript")
    context["obj"] = obj
    
    return render(request, template_name, context)


def mark_delete(request, pk):
    context = {}
    template_name = "ctrl_comb/mark-list.html"
    
    o = Mark.objects.filter(id=pk).first()
    o.delete()  # type: ignore
    
    obj = Mark.objects.all().order_by("decript")
    context["obj"] = obj
    
    return render(request, template_name, context)