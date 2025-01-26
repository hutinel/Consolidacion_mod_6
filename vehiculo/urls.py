from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('listar/', views.listar, name='listar'),
    ]