import re
from store.lists import *


def process_markdown(text, in_appendices=False):
    markdown_content = ''
    # Función para agregar "#" delante de las palabras encontradas

    def agregar_hashtag(match):
        return f"# {match.group(0)}\n"

    # Eliminar encabezados y pies de página
    text = re.sub(
        r'(\n|\s|^)([0-9]+|www\..+\.es)(\s|\n|$)', ' ', text, flags=re.MULTILINE)

    # Eliminar imágenes
    text = re.sub(r'\[image:.+?\]', '', text)

    # Eliminar guiones y saltos de línea subsiguientes
    text = re.sub(r'-\n', '', text)

    # Eliminar el contenido entre "FIRMADO POR" y "Es copia auténtica de documento electrónico"
    text = re.sub(r'FIRMADO POR.*?Es copia auténtica de documento electrónico',
                  '', text, flags=re.DOTALL)

    # Expresión regular para buscar el patrón "letra, paréntesis) y espacio"
    text = re.sub(r'([a-zA-Z])\)\s', '* ', text)

    # Elimina los cuadrados de eleccion vacios
    text = re.sub("˘", 'Falso: ', text)

    # Elimina el cuadrado de eleccion marcado (pero no la respuesta)
    text = re.sub("⾙", 'Verdadero: ', text)

    # Convertir los Artículos en títulos para las secciones
    text = re.sub(r'Artículo', '# Artículo', text)
    text = re.sub(r'INSTRUCCIONES', '# INSTRUCCIONES', text)

    # Patrón para buscar las palabras en la lista
    patron = re.compile(
        r'\b(?:' + '|'.join(map(re.escape, list_order_fem)) + r')\b')

    # Reemplazar las palabras con "#" delante
    text = patron.sub(agregar_hashtag, text)

    # Patrón para buscar las palabras en la lista
    patron = re.compile(
        r'\b(?:' + '|'.join(map(re.escape, list_order_masc)) + r')\b')

    # Reemplazar las palabras con "#" delante
    text = patron.sub(agregar_hashtag, text)

    # Patrón para buscar las palabras en la lista
    patron = re.compile(
        r'\b(?:' + '|'.join(map(re.escape, list_romanos)) + r')\b')

    # Reemplazar las palabras con "#" delante
    text = patron.sub(agregar_hashtag, text)

    # Check if we are in the appendices section
    if re.search(r'ANEXO', text):
        in_appendices = True

    # Exclude the appendices section from the final content
    if not in_appendices:
        markdown_content += text

    return markdown_content
