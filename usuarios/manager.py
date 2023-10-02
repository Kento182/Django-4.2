from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, username, first_name, password, **kwargs):
        now = timezone.now()
        
        if not email:
            raise ValueError(_("Email es requerido"))        
        if not first_name:
            raise ValueError(_("El nombre es requerido"))
        
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            username = username,
            first_name = first_name,
            last_login = now,
            **kwargs
            )
        user.setpassword(password)
        user.save(using=self._db)
        return user
        
    def create_user(self,email,username,first_name,password,**kwargs):
        return self._create_user(email,username,first_name,password,**kwargs)
    
    def create_superuser(self,email,username,first_name,password,**kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_superuser',True)
        kwargs.setdefault('is_active',True)

        if kwargs.get("is_staff") is not True:
            raise ValueError(_("is_staff debe ser True para ser super usuario"))
        
        if kwargs.get("is_superuser") is not True:
            raise ValueError(_("is_superuser debe ser True para ser super usuario"))
        
        return self._create_user(email,username,first_name,password,**kwargs)
