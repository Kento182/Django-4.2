from django.urls import path
from .views import *


urlpatterns = [
    path('mark/', MarkList.as_view(), name="mark_list"),
    path('mark/save', mark_save, name="mark_save"),
]
