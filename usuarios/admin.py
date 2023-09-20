from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

UsuarioPersonalizado = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UsuarioPersonalizado
    list_display = [
        "email",
        "username",
        "is_superuser"
    ]
    

admin.site.register(UsuarioPersonalizado, CustomUserAdmin)