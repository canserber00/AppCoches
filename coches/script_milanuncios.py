from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from .models import Coche

# Función para scrapear coches desde Milanuncios utilizando Selenium
def scrape_milanuncios():
    # Ruta al ChromeDriver (ajusta esta ruta según donde hayas descargado chromedriver)
    chrome_service = Service('/ruta/a/chromedriver')  # Cambia esto por la ruta correcta
    
    # Configurar opciones del navegador
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Si no quieres que el navegador sea visible
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Iniciar el navegador
    driver = webdriver.Chrome(service=chrome_service, options=options)

    # Cargar la página de Milanuncios
    url = 'https://www.milanuncios.com/coches-de-segunda-mano-en-galicia/santiago-compostela.htm'
    print("Iniciando scraping en:", url)
    driver.get(url)

    # Esperar a que la página cargue
    time.sleep(5)

    # Obtener el HTML de la página
    html = driver.page_source
    print("HTML de la página recibido")

    # Usar BeautifulSoup para parsear el HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar los anuncios en el HTML
    anuncios = soup.find_all('a', class_='ma-AdCardListingV2-TitleLink')
    print(f"Se encontraron {len(anuncios)} anuncios")

    for anuncio in anuncios:
        try:
            # Extraer el enlace del anuncio
            enlace = anuncio['href']
            enlace_completo = f"https://www.milanuncios.com{enlace}"
            print(f"Accediendo al anuncio: {enlace_completo}")

            # Navegar a la página del anuncio individual
            driver.get(enlace_completo)
            time.sleep(3)  # Esperar a que cargue el anuncio individual

            # Extraer el HTML del anuncio
            anuncio_html = driver.page_source
            anuncio_soup = BeautifulSoup(anuncio_html, 'html.parser')

            # Extraer el modelo desde el <h2> del anuncio completo
            modelo = anuncio_soup.find('h2', class_='ma-SharedText ma-AdCardV2-title ma-SharedText--m ma-SharedText--Black ma-SharedText--numLines').text.strip()
            print(f"Modelo: {modelo}")

            # Extraer el precio
            precio = anuncio_soup.find('span', class_='ma-AdPrice-value').text.strip()
            precio = int(precio.replace('€', '').replace('.', '').strip())
            print(f"Precio: {precio}")

            # Extraer año y kilometraje
            detalles = anuncio_soup.find_all('span', class_='ma-AdTag-label')
            año = 0
            kilometraje = 0
            for detalle in detalles:
                texto = detalle.text.strip()
                if 'kms' in texto:
                    kilometraje = int(texto.replace('kms', '').replace('.', '').strip())
                elif '20' in texto:  # Años como 2015, 2020
                    año = int(texto)
            print(f"Año: {año}, Kilometraje: {kilometraje} kms")

            # Guardar en la base de datos
            coche = Coche(marca=modelo, modelo=modelo, año=año, precio=precio)
            coche.save()
            print("Coche guardado correctamente")

        except AttributeError as e:
            print(f"Error al extraer información de un anuncio: {e}")
            continue

    # Cerrar el navegador
    driver.quit()

    print("Scraping completado y datos guardados.")
