import PyPDF2 
import tabula
import re

import warnings
warnings.filterwarnings('ignore')

lista_tabelas = tabula.read_pdf('relatorio.pdf', pages='all')

'''
print(len(lista_tabelas))

tabela1 = lista_tabelas[0]
print(tabela1)

print(tabela7)
'''
tabela7 = lista_tabelas[6]

texto = tabela7['coluna_interessante'].to_string(index=False)

padrao = r'pagador\s+([A-Z][a-z]+(?: [A-Z][a-z]+)*)'

padrao1 = re.findall(padrao, tabela7)

print(padrao1)