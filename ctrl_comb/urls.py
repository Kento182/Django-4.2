from django.urls import path
from .views import *

urlpatterns = [
    path('mark/', MarkList.as_view(), name="mark_list"),    
    path('mark/save', mark_save, name="mark_save"),
    path('mark/delete/<int:pk>', mark_delete, name="mark_delete"),
    path('mark/edit/<int:pk>', mark_edit, name="mark_edit"),
    
    path('models/', ModeloList.as_view(), name="modelo_list"),
    path('models/new', ModeloNew.as_view(), name="modelo_new"),    
    path('models/new-modal', ModeloNewModal.as_view(), name="modelo_new_modal"),    
    path('models/edit/<int:pk>', ModeloEdit.as_view(), name="modelo_edit"),
    path('models/edit-modal/<int:pk>', ModeloEditModal.as_view(), name="modelo_edit_modal"),
    path('models/delete/<int:pk>', ModeloDelete.as_view(), name="modelo_delete"),
    path("models/dt", modelo_dt, name="modelo_dt"),
    
    path('vehicles/', VehiculoList.as_view(), name="vehiculo_list"),
    path('vehicles/dt', vehiculo_dt, name="vehiculo_dt"),
    path('vehicles/new', VehiculoNewModal.as_view(), name="vehiculo_new"),
    path('vehicles/edit/<int:pk>', VehiculoEditModal.as_view(), name="vehiculo_edit"),
    path('vehicles/delete/<int:pk>', VehiculoDelete.as_view(), name="vehiculo_delete"),
]
