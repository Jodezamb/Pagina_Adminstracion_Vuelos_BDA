from django.urls import path
from . import views

urlpatterns =[
    path('',views.inicio, name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('vuelos',views.vuelos,name='vuelos'),
    path('vuelos/crear',views.crear,name='crear'),
    path('vuelos/editar',views.editar,name='editar'),
    
    ]