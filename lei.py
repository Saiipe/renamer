import tabula.io
import re

# Ler o PDF
pdf2 = tabula.io.read_pdf('danfe.pdf')

# Definir o padrão de expressão regular para o nome
meu_nome = "ITAUAN SANTOS DE JESUS"  # Substitua por seu nome real
padrao_nome = re.compile(r'\b{}\b'.format(re.escape(meu_nome)))

# Inicializar uma variável para armazenar se o nome foi encontrado
nome_encontrado = False

# Iterar sobre as partes do PDF
for df in pdf2:
    # Converter o DataFrame para uma string
    texto_df = df.to_string(index=False, header=False)
    # Verificar se o padrão do nome está presente no texto
    if padrao_nome.search(texto_df):
        nome_encontrado = True
        break

# Verificar se o nome foi encontrado
if nome_encontrado:
    print("Seu nome foi encontrado no PDF.", )
else:
    print("Seu nome não foi encontrado no PDF.")
