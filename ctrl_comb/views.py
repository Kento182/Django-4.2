from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *
from .forms import *


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
        o = None
        
        if i:
            o = Mark.objects.filter(id=i).first()
        else:
            o = Mark.objects.filter(decript = d)
            
        if o:
            o.decript = d   # type: ignore
            o.save()    # type: ignore
        else:                 
            o = Mark.objects.create(decript = d)
            
    obj = Mark.objects.all().order_by("decript")    
    context["obj"] = obj
    context["reg"] = o  # type: ignore
    
    return render(request, template_name, context)


def mark_delete(request, pk):
    context = {}
    template_name = "ctrl_comb/mark-list.html"
    
    o = Mark.objects.filter(id=pk).first()
    o.delete()  # type: ignore
    
    obj = Mark.objects.all().order_by("decript")
    context["obj"] = obj
    
    return render(request, template_name, context)


def mark_edit(request, pk=None):
    context = {}
    template_name = "ctrl_comb/mark-frm.html"
    
    if pk:
        o = Mark.objects.filter(id=pk).first()
        frm = MarkForm(instance=o)
    else:
        frm = MarkForm()
        
    context["form"] = frm
    context["obj"] = o  # type: ignore
    return render(request, template_name, context)


class ModeloList(ListView):
    template_name="ctrl_comb/modelo.html"
    model=Modelo
    context_object_name="obj"
    ordering=["mark","descript"]
    
    
class ModeloNew(CreateView):
    template_name="ctrl_comb/modelo_form.html"
    model=Modelo
    context_object_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("control:modelo_list")
    

class ModeloEdit(UpdateView):
    template_name="ctrl_comb/modelo_form.html"
    model=Modelo
    context_object_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("control:modelo_list")
    

class ModeloDelete(DeleteView):
    template_name="bases/delete.html"
    model=Modelo
    context_object_name="obj"    
    success_url=reverse_lazy("control:modelo_list")
    

class ModeloEditModal(UpdateView):
    template_name="ctrl_comb/modelo_modal.html"
    model=Modelo
    context_object_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("control:modelo_list")
    

class ModeloNewModal(CreateView):
    template_name="ctrl_comb/modelo_modal.html"
    model=Modelo
    context_object_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("control:modelo_list")