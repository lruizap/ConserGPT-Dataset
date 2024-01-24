import io
import requests
from PyPDF2.errors import PdfReadError
from PyPDF2 import PdfReader

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Windows; Windows x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}


def process_pdf(link_pdf):
    try:
        response = requests.get(url=link_pdf, headers=headers, timeout=120)
        on_fly_mem_obj = io.BytesIO(response.content)
        return PdfReader(on_fly_mem_obj)
    except PdfReadError as e:
        error_message = f"Error reading PDF ({link_pdf}): {e}"
        print(error_message)
        with open("../out/logs.txt", "a", encoding="utf-8") as logs_file:
            logs_file.write(error_message + "\n")
        return None
