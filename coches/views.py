from django.shortcuts import render, redirect
from .script_milanuncios import scrape_milanuncios
from .models import Coche  # Importa el modelo Coche


def scrapear_milanuncios(request):
    # Ejecutar el scraping de Milanuncios
    scrape_milanuncios()
    
    # Redirigir a la lista de coches después del scraping
    return redirect('lista_coches')

# Vista para mostrar la lista de coches
def lista_coches(request):
    coches = Coche.objects.all()  # Recupera todos los coches de la base de datos
    return render(request, 'coches/lista_coches.html', {'coches': coches})


