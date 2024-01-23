from store.process_markdown import process_markdown


def process_text(pdf_file, in_appendices):
    try:
        markdown = ''
        for pageNum in range(len(pdf_file.pages)):
            currentPage = pdf_file.pages[pageNum]
            text = currentPage.extract_text()
            markdown = markdown + \
                process_markdown(text=text, in_appendices=in_appendices)

        return markdown

    except Exception as e:
        error_message = f"Error al recorrer las páginas del : {e}"
        print(error_message)
        with open("../out/logs.txt", "a", encoding="utf-8") as logs_file:
            logs_file.write(error_message + "\n")
        return ''
