import pytesseract
import cv2
import re

imagem = cv2.imread("pagina_1.jpg")

caminho = r"C:\Users\itaua\AppData\Local\Programs\Tesseract-ORC"
pytesseract.pytesseract.tesseract_cmd= caminho + r'\tesseract.exe'

texto = pytesseract.image_to_string(imagem)

linhas = texto.split('\n')
frase = ' '.join(linhas)

padrao_cpf = r'\d{3}.\d{3}.\d{3}-\d{2}'
correspondencia = re.findall(padrao_cpf,frase)
numero_cpf = set(correspondencia)

padrao_nome = r'pagador:\s+([^-\n]+)'
correspondencia1 = re.findall(padrao_nome, frase)
nome_social = set(correspondencia1)

padrao_valor = r'Valor do Documento (\d+,\d+) \d+ \(-\)'
correspondencia2 = re.findall(padrao_valor, frase)
valor_bol = set(correspondencia2)

#print (frase)
print (correspondencia)
print (correspondencia1)
print(correspondencia2)



