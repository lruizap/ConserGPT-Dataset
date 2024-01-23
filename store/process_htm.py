from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import html2text

from store.process_markdown import process_markdown


def process_htm(url):
    try:
        # Configurar el path del chromedriver (ajusta la ruta según tu configuración)
        # path_chromedriver = "RUTA/AL/CHROMEDRIVER"

        # Configurar las opciones del navegador
        opciones = Options()
        # Ejecutar en modo sin cabeza (sin interfaz gráfica)
        opciones.add_argument('--headless')

        # Iniciar el navegador Chrome con la ruta del chromedriver
        driver = webdriver.Chrome(options=opciones)

        # Realizar una solicitud a la URL
        driver.get(url)

        driver.implicitly_wait(1)

        # Obtener el código fuente HTML
        codigo_html = driver.page_source

        # Cerrar el navegador
        driver.quit()

        # Parsear el HTML con BeautifulSoup
        soup = BeautifulSoup(codigo_html, 'html.parser')

        # Obtener el texto sin etiquetas HTML
        texto_plano = soup.get_text(separator=' ', strip=True)

        # Convertir a Markdown usando html2text
        markdown_text = html2text.html2text(texto_plano)

        return process_markdown(markdown_text)

    except Exception as e:
        error_message = f"Error al obtener o transformar el contenido: {e}"
        print(error_message)
        with open("../out/logs.txt", "a", encoding="utf-8") as logs_file:
            logs_file.write(error_message + "\n")
        return None
