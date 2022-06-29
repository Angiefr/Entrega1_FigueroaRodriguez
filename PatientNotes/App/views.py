from django.shortcuts import render, redirect
from .models import Medicamento, Tratamiento, Doctor

# Create your views here.

def home(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'index.html', {'medicamentos': medicamentos})

def inicio(request):
    nombre = request.POST('txtNombre')
    medicamentos = Medicamento.objects.create(nombre = nombre)
    return redirect('/')