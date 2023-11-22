from django.db import models

from bases.models import ClaseModelo


class Mark(ClaseModelo):
    decript = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.decript
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        

class Modelo(ClaseModelo):
    descript = models.CharField(max_length=50, db_comment="Descripción del Modelo del Vehículo")    #type: ignore
    mark = models.ForeignKey(Mark, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.mark} - {self.descript}"
    
    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
        db_table_comment = "Modelos de Vehiculos"