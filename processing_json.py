from store.lists import *
from store.open_json import open_json
from store.process_htm import process_htm
from store.process_pdf import process_pdf
from store.process_text import process_text
from store.save_markdown_file import save_markdown_file
from store.process_imagePdf import process_imagePdf

json_path = "./JSON/ConserGPT_DATA.json"
logs_path = './out/logs.txt'

with open(logs_path, 'w', encoding='utf-8') as archivo_logs:
    archivo_logs.write('')


def process_modules(data):
    try:
        for module_key, module_value in data["modules"].items():
            print("\nTrabajando en la letra:", module_key, '\n')
            for info in module_value["Info"]:
                for pdf_info in info["ListPDF"]:
                    link_pdf = pdf_info["LinkPDF"].lower()

                    link_pdf = link_pdf.lower()

                    if link_pdf.endswith('.pdf'):
                        pdf_file = process_pdf(link_pdf)

                        in_appendices = False
                        markdown_content = process_text(
                            pdf_file, in_appendices)

                    elif link_pdf.endswith('.htm'):
                        markdown_content = process_htm(link_pdf)
                    else:
                        # wordSearch = "Circular"
                        # if wordSearch.lower() in link_pdf.lower():
                        print(link_pdf)
                        pdf_file = process_imagePdf(link_pdf)

                    if pdf_file is None:
                        continue

                    pdf_file.stream.close()
                    save_markdown_file(markdown_content, link_pdf)

    except Exception as e:
        error_message = f"An error occurred: {e}"
        with open("./out/logs.txt", "a", encoding="utf-8") as logs_file:
            logs_file.write(error_message + "\n")
        return None


# Example usage
data = open_json(json_path)
if data is not None:
    process_modules(data)
