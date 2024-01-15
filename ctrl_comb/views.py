from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser

from .models import *
from .forms import *
from bases.views import SinAutorizacion, MixinSaveUser


# class MarkList(LoginRequiredMixin, ListView):
class MarkList(SinAutorizacion, ListView):
    template_name="ctrl_comb/mark.html"
    model=Mark
    context_object_name="obj"
    ordering=["decript"]
    login_url="usuarios:login"
    permission_required="ctrl_comb.view_mark"
    

def mark_save(request):
    context = {}
    template_name = "ctrl_comb/mark-list.html"
    
    if request.method == "POST":
        i = request.POST.get("id")
        d = request.POST.get("decript")
        u = request.user
        o = None
        
        if i:
            o = Mark.objects.filter(id=i).first()
        else:
            o = Mark.objects.filter(decript = d)
            
        if o:
            o.decript = d   # type: ignore
            o.um = u    # type: ignore
            o.save()    # type: ignore
        else:                 
            o = Mark.objects.create(decript = d, uc = u)
            
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


# class ModeloList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class ModeloList(SinAutorizacion, ListView):
    template_name="ctrl_comb/modelo.html"
    model=Modelo
    context_object_name="obj"
    ordering=["mark","descript"]
    login_url="usuarios:login"
    permission_required="ctrl_comb.view_modelo"
    # raise_exception=False
    # redirect_field_name="redirect_to"
    
    # def form_invalid(self, form):
    #     response = super().form_invalid(form)   # type: ignore
    #     if self.request.is_ajax():
    #         return JsonResponse(form.errors,status=400)
    #     else:
    #         return response
    
    # def handle_no_permission(self):
    #     if not self.request.user == AnonymousUser():
    #         self.login_url = "pages:forbidden"
    #     return HttpResponseRedirect(reverse_lazy(self.login_url))
    
    
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
    

class ModeloEditModal(SinAutorizacion, MixinSaveUser ,UpdateView):
    template_name="ctrl_comb/modelo_modal.html"
    model=Modelo
    context_object_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("control:modelo_list")
    login_url="usuarios:login"
    permission_required="ctrl_comb.change_modelo"
    
    # def form_valid(self, form):
    #     if form.instance.id:
    #         form.instance.um = self.request.user
    #     else:
    #         form.instance.uc = self.request.user
            
    #     return super().form_valid(form)
        

class ModeloNewModal(SinAutorizacion, MixinSaveUser, CreateView):
    template_name="ctrl_comb/modelo_modal.html"
    model=Modelo
    context_object_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("control:modelo_list")
    login_url="usuarios:login"
    permission_required="ctrl_comb.add_modelo"
    
    # def form_valid(self, form):
    #     if form.instance.id:
    #         form.instance.um = self.request.user
    #     else:
    #         form.instance.uc = self.request.user
            
    #     return super().form_valid(form)
    

@login_required(login_url="usuarios:login")
@permission_required("ctrl_comb.view_modelo")
def modelo_dt(request):
    context = {}
    datos = request.GET
    
    draw = int(datos.get("draw"))
    start = int(datos.get("start"))
    length = int(datos.get("length"))
    search = datos.get("search[value]")
    
    registros = Modelo.objects.all()
    
    if search:
        registros = registros.filter(
            Q(mark__decript__icontains=search) |
            Q(descript__icontains=search)
        )
        
    recordsTotal = registros.count()
    # recordsFiltered = recordsTotal
    
    context["draw"] = draw
    context["recordsTotal"] = recordsTotal
    context["recordsFiltered"] = recordsTotal
    
    reg = registros[start:start + length]
    paginator = Paginator(reg,length)
    
    try:
        obj = paginator.page(draw).object_list
    except PageNotAnInteger:
        obj = paginator.page(draw).object_list
    except EmptyPage:
        obj = paginator.page(paginator.num_pages).object_list
        
    # datos = []
    # for o in obj:
    #     datos.append({"id":o.id, "mark":o.mark.decript, "descript":o.descript})
    
    datos = [
        {
            "id" : o.id, "mark":o.mark.decript, "descript":o.descript
        } for o in obj
    ]
    
    context["datos"] = datos
    return JsonResponse(context,safe=False)


class VehiculoList(SinAutorizacion, TemplateView):
    template_name="ctrl_comb/vehiculo.html"
    login_url="core:home"
    permission_required="ctrl_comb.view_vehiculo"
    

@login_required(login_url="usuarios:login")
@permission_required("ctrl_comb.view_vehiculo")
def vehiculo_dt(request):
    context = {}
    datos = request.GET
    
    draw = int(datos.get("draw"))
    start = int(datos.get("start"))
    length = int(datos.get("length"))
    search = datos.get("search[value]")
    
    if request.user.is_superuser:
        registros = Vehiculo.objects.all()
    else:
        registros = Vehiculo.objects.filter(uc = request.user)
    
    if search:
        registros = registros.filter(
            Q(modelo__mark__decript__icontains=search) |
            Q(modelo__descript__icontains=search) |
            Q(register__icontains=search) |
            Q(year__icontains=search)
        )
        
    recordsTotal = registros.count()
    # recordsFiltered = recordsTotal
    
    context["draw"] = draw
    context["recordsTotal"] = recordsTotal
    context["recordsFiltered"] = recordsTotal
    
    reg = registros[start:start + length]
    paginator = Paginator(reg,length)
    
    try:
        obj = paginator.page(draw).object_list
    except PageNotAnInteger:
        obj = paginator.page(draw).object_list
    except EmptyPage:
        obj = paginator.page(paginator.num_pages).object_list
        
    datos = [
        {
            "id" : o.id, "mark":o.modelo.mark.decript, "modelo":o.modelo.descript,
            "register":o.register, "year":o.year
        } for o in obj
    ]
    
    context["datos"] = datos
    return JsonResponse(context,safe=False)


class VehiculoNewModal(SinAutorizacion, MixinSaveUser, CreateView):
    template_name="ctrl_comb/vehiculo_modal.html"
    model=Vehiculo
    context_object_name="obj"
    form_class=VehiculoForm
    success_url=reverse_lazy("control:vehiculo_list")
    login_url="usuarios:login"
    permission_required="ctrl_comb.add_vehiculo"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["marcas"] = Mark.objects.all()
        context["modelos"] = Modelo.objects.all()
        return context
    
class VehiculoEditModal(SinAutorizacion, MixinSaveUser ,UpdateView):
    template_name="ctrl_comb/vehiculo_modal.html"
    model=Vehiculo
    context_object_name="obj"
    form_class=VehiculoForm
    success_url=reverse_lazy("control:vehiculo_list")
    login_url="usuarios:login"
    permission_required="ctrl_comb.change_vehiculo"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["marcas"] = Mark.objects.all()
        context["modelos"] = Modelo.objects.all()
        return context
    
    
class VehiculoDelete(DeleteView):
    template_name="bases/delete.html"
    model=Vehiculo
    context_object_name="obj"    
    success_url=reverse_lazy("control:vehiculo_list")