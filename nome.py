
import tabula
import PyPDF2
import re

arquivo_pdf = open('teste1.pdf', 'rb')
pdf = PyPDF2.PdfReader(arquivo_pdf)

pagina = pdf.pages[0]
texto = pagina.extract_text();
lista_palavras = texto.split()  # Dividindo o texto em uma lista de palavras
texto_com_hifen = '-'.join(lista_palavras)  # Juntando as palavras usando hífen como separador
meu = "109.581.285-88"
corres = re.search(meu, texto_com_hifen)

print(texto_com_hifen)

print(corres.group())


arquivo_pdf = open('teste1.pdf', 'rb')
pdf = PyPDF2.PdfReader(arquivo_pdf)

pagina = pdf.pages[0]
texto = pagina.extract_text();
lista_palavras = texto.split()  # Dividindo o texto em uma lista de palavras
texto_com_hifen = '-'.join(lista_palavras)  # Juntando as palavras usando hífen como separador
corres = re.search(cpf, texto_com_hifen)

cpf2 = corres.group()

for jpg in img :
