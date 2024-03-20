from django import forms

from .models import *


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            
            
class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ["mark","descript"]
        
        
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ["modelo","register","year","tipo","unidad_medida"]