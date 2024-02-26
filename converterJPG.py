from pdf2image import convert_from_path

# Caminho para o arquivo PDF
pdf_path = 'relatorio.pdf'

# Converter PDF em uma lista de imagens JPEG
images = convert_from_path(pdf_path)

# Salvar cada imagem como um arquivo JPEG
for i, image in enumerate(images):
    image.save(f'pagina_{i + 1}.jpg', 'JPEG')
