import PyPDF2 
import tabula

import warnings
warnings.filterwarnings('ignore')

lista_tabelas = tabula.read_pdf('relatorio.pdf', pages='all')

print(len(lista_tabelas))

for tabela in lista_tabelas:
    print(tabela)