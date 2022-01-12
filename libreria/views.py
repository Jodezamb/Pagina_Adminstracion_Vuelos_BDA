from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')
# directamente a template haciendo una solicitud a traves dela url  

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def vuelos(request):
    return render(request, 'vuelos\index.html')

def crear(request):
    return render(request, 'vuelos/crear.html')