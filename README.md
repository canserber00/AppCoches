# AppCoches

AppCoches es un proyecto Django para scrapear coches usados desde Milanuncios y almacenarlos en una base de datos. Este proyecto incluye:
- Una aplicación Django llamada **coches**.
- Scraping utilizando **BeautifulSoup** (próximamente Selenium).
- Modelos, vistas y plantillas para mostrar los coches en una tabla estilizada con Bootstrap.

## Requisitos

- Python 3.x
- Django
- BeautifulSoup
- Selenium (para la versión futura de scraping con navegador)

## Cómo ejecutar el proyecto

1. Clona el repositorio:
    ```bash
    git clone https://github.com/canserber00/AppCoches.git
    cd AppCoches
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Aplica las migraciones:
    ```bash
    python manage.py migrate
    ```

4. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

5. Visita `http://127.0.0.1:8000/coches/` para ver la lista de coches scrapeados.

## Próximos pasos

- Integrar Selenium y ChromeDriver para evitar bloqueos de scraping.
