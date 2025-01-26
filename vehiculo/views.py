from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo

# Create your views here.
def index(request):
    return render(request, 'vehiculo/index.html')

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})


def listar(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar.html', {'vehiculos': vehiculos})