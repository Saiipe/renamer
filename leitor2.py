import PyPDF2
import re

pdf = PyPDF2.PdfReader('relatorio.pdf')
all_text = ""

for page in pdf.pages:
    text = page.extract_text()
    all_text += (text + "\n")


    

padrao_cpf = r'\d{3}.\d{3}.\d{3}-\d{2}'
correspondencia = re.findall(padrao_cpf,all_text)
numero_cpf = set(correspondencia)
