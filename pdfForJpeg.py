import os

# Obtém o nome de usuário do sistema
nome_usuario = os.getlogin()

# Constrói o caminho para o diretório "img" dentro da pasta "Documentos"
caminho_img = os.path.join("C:\\Users", nome_usuario, "Documents", "img")

# Cria o diretório "img" se não existir
if not os.path.exists(caminho_img):
    os.makedirs(caminho_img)
