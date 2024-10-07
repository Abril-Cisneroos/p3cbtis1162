from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def sucursales(request):
    return render(request, "sucursales.html")

def mascotas(request):
    return render(request, "mascotas.html")

def empleados(request):
    return render(request, "empleados.html")

