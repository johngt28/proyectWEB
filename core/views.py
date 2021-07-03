from core.forms import ContactoForm
from django.shortcuts import render
from .models import contacto

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def Artistas(request):
    return render(request,'core/Artistas.html')

def galeria(request):
    return render(request,'core/galeria.html')

def log_in(request):
    return render(request,'core/log_in.html')

def perfil_art(request):
    return render(request,'core/perfil_art.html')

#def registro(request):
#    return render(request,'core/registro.html')

def registro(request):
    datos = {
        'form': ContactoForm()
    }
    if request.method== 'POST':
        contact_us = ContactoForm(request.POST)
        if contact_us.is_valid:
            contact_us.save()
    return render(request, 'core/registro.html',datos)
