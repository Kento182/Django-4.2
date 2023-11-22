from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse_lazy

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class HomeView(TemplateView):
    template_name = "bases/home.html"


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


class MixinFormInvalid:
    def form_invalid(self, form):
         response = super().form_invalid(form)  # type: ignore
         if is_ajax(request=self.request):  # type: ignore
             return JsonResponse(form.errors,status=400)
         else:
             return response
         

class SinAutorizacion(LoginRequiredMixin, PermissionRequiredMixin, MixinFormInvalid):
    login_url = "bases:login"
    raise_exception = False
    redirect_field_name = "redirect_to"
    
    def handle_no_permission(self):
        if not self.request.user == AnonymousUser():    # type: ignore
            self.login_url = "pages:forbidden"
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class MixinSaveUser:
    def form_valid(self, form):
        if form.instance.id:
            form.instance.um = self.request.user    # type: ignore
        else:
            form.instance.uc = self.request.user    # type: ignore
            
        return super().form_valid(form) # type: ignore