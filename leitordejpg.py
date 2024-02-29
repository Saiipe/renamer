import pytesseract
import cv2
import re

# Carrega a imagem
imagem = cv2.imread("img/relatorio.pdf1.jpg")

# Definir o caminho para o executável do Tesseract OCR
caminho = r"C:\Users\itaua\AppData\Local\Programs\Tesseract-ORC"
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'

# Use o pytesseract para extrair texto da imagem
texto = pytesseract.image_to_string(imagem)

# Definir padrões regex para encontrar o valor do documento
padrao_inicio = re.compile(r'1 \(=\) Valor do Documento\s*:\s*(\d+\.\d+,\d+)')
padrao_fim = re.compile(r'2 \(-\) Desconto / Abatimento')

# Procurar o padrão de início no texto
correspondencia_inicio = padrao_inicio.search(texto)

# Procurar o padrão de fim no texto
correspondencia_fim = padrao_fim.search(texto)

# Se ambas as correspondências forem encontradas, extrair o valor do documento
if correspondencia_inicio and correspondencia_fim:
    inicio_valor = correspondencia_inicio.start()
    fim_valor = correspondencia_fim.start()
    valor_documento = texto[inicio_valor:fim_valor].split(":")[-1].strip()
    print("Valor do Documento:", valor_documento)
else:
    print("Valor do Documento não encontrado.")
