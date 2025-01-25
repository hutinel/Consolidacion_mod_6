from django.shortcuts import render
from .models import Vehiculo

# Create your views here.
def index(request):
    return render(request, 'vehiculo/index.html')