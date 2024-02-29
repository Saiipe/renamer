
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

# Definir padrão regex para encontrar o valor do documento
valorDoc = re.compile(r'RS t\s*(\d+,\d+)')
padrao_nome= re.compile(r'Pagador\s*:\s*([^\-]+)\s*-')
padrao_cpf = re.compile(r'(\d{3}\.\d{3}\.\d{3}-\d{2})')



# Procurar o padrão no texto
correspondencia = valorDoc.search(texto)
correspondencia1 = padrao_nome.search(texto)
correspondencia2 = padrao_cpf.search(texto)

# Se a correspondência for encontrada, extrair o valor do documento
if correspondencia:
    valor_documento = correspondencia.group(1)
    print("Valor do Documento:", valor_documento)
else:
    print("Valor do Documento não encontrado.")

print (correspondencia2)