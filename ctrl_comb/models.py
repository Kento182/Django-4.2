from django.db import models
from django.urls import reverse
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
        
        
class Vehiculo(ClaseModelo):
    modelo = models.ForeignKey(Modelo, on_delete=models.RESTRICT)
    register = models.CharField(max_length=50, db_column="Matricula Vehículo", help_text="Matricula Vehículo")
    year = models.PositiveSmallIntegerField(help_text="Año del Vehículo")
    
    TIPO_CHOICES = [
        ('MOT', 'Motocicleta'),
        ('CAP', 'Caponera'),
        ('SUV', 'Camioneta (SUV)'),
        ('PIK', 'PickUp'),
        ('SED', 'Sedán'),
        ('TAX', 'Taxi'),
        ('MIC', 'Microbus'),
        ('BUS', 'Autobus'),
        ('CAM', 'Camion')
    ]
    tipo = models.CharField(choices=TIPO_CHOICES, max_length=3, default='SED')
    
    class UnidadMedida(models.IntegerChoices):
        GALONES = 1
        LITROS = 2
        
    unidad_medida = models.IntegerField(choices=UnidadMedida.choices, default=1)
    
    @property
    def factor(self):
        f = 1
        if self.unidad_medida == 2:
            f = .264172
        return f
    
    def __str__(self):
        return self.register
    
    def get_absolute_url(self):
        return reverse("vehiculo_edit",kwargs={'pk':self.pk})
    
    class Meta:
        verbose_name_plural = "Vehículos"
        db_table_comment = "Vehículos"