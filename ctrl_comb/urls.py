from django.urls import path
from .views import *

urlpatterns = [
    path('mark/', MarkList.as_view(), name="mark_list"),
    path('mark/save', mark_save, name="mark_save"),
    path('mark/delete/<int:pk>', mark_delete, name="mark_delete"),
    path('mark/edit/<int:pk>', mark_edit, name="mark_edit"),
    
    path('models/', ModeloList.as_view(), name="modelo_list"),
]
