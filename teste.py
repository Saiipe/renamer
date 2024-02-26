import re

# Texto extraído da imagem
texto = "Este é um exemplo de texto com um número de telefone: (123) 456-7890."

# Expressão regular para encontrar números de telefone no formato (123) 456-7890
padrao_telefone = r'\(\d{3}\) \d{3}-\d{4}'

# Procurar por números de telefone no texto usando a expressão regular
numeros_telefone = re.findall(padrao_telefone, texto)

# Imprimir os números de telefone encontrados
print("Números de telefone encontrados:")
for telefone in numeros_telefone:
    print(telefone)
