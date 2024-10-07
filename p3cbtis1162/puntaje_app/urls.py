from django.urls import path
from . import views
urlpatterns = [
    path ("",views.index,name="index"),
    path ("sucursales/",views.sucursales,name="sucursales"),
    path ("mascotas/",views.mascotas,name="mascotas"),
    path ("empleados/",views.empleados,name="empleados"),
]