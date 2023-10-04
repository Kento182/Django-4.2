from django.db import models


class Mark(models.Model):
    decript = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.decript
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"