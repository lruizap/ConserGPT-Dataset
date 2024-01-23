def save_markdown_file(markdown_content, link_pdf):
    if len(markdown_content) < 1:
        return

    if "https" in link_pdf:
        newName = link_pdf.replace('https://www.adideandalucia.es/normas/', '')
    else:
        newName = link_pdf.replace('http://www.juntadeandalucia.es/', '')

    newName = newName.replace('.pdf', '.md')
    newName = newName.replace('.htm', '.md')
    newName = newName.replace('/', '_')

    with open(f"./out/documents/{newName}", "w", encoding="utf-8") as markdown_file:
        markdown_file.write(markdown_content)

    print("Conversion complete. Markdown file generated:", {link_pdf})
