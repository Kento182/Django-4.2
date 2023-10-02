from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import *

app_name="usuarios"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login2/', auth_views.LoginView.as_view(template_name="usuarios/login2.html"), name="login2"),
    path('registro/', RegistroUsuarioView.as_view(), name="registro"),
]
