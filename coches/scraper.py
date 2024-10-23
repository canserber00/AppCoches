import requests
from bs4 import BeautifulSoup
from .models import Coche

# Función para scrapear coches desde Milanuncios en Galicia
def scrape_milanuncios():
    url = 'https://www.milanuncios.com/coches-de-segunda-mano-en-galicia/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Ajusta estos selectores según el HTML de Milanuncios
        anuncios = soup.find_all('article', class_='aditem')

        for anuncio in anuncios:
            try:
                marca = anuncio.find('h2').text.strip()  # Cambia el selector si es necesario
                modelo = anuncio.find('h3').text.strip()  # Cambia el selector si es necesario
                precio = anuncio.find('div', class_='aditem-price').text.strip().replace('€', '').replace('.', '').strip()
                año = anuncio.find('div', class_='aditem-detail').text.split(' ')[0]  # Esto también debe ajustarse según el HTML
                
                # Guardar en la base de datos
                coche = Coche(marca=marca, modelo=modelo, año=int(año), precio=int(precio))
                coche.save()
            except AttributeError:
                # Omitir anuncios mal formados o incompletos
                continue

        print("Scraping completado y datos guardados.")
    else:
        print(f"Error al obtener la página: {response.status_code}")


