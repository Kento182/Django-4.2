from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    fc = models.DateTimeField(auto_now_add=True)
    um = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="+", blank=True, null=True)
    fm = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
