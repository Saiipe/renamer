import os
import pytesseract
import cv2
import re
import PyPDF2
import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path

# Abrir uma janela para seleção de múltiplos arquivos
root = tk.Tk();
root.withdraw();
# Solicitar os caminhos dos arquivos PDF
pdf_paths = filedialog.askopenfilenames();
# Diretório onde as imagens serão salvass
diretorio_destino = "Img";
# Lista para armazenar os caminhos do arquivos JPEG criados
jpeg_paths = [];
# Converter cada PDF em imagens JPEG
for pdf_path in pdf_paths:
    images = convert_from_path(pdf_path);
    # Certifique-se de que o diretório de destino existe, se não, crie-o
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino);
    # Salvar as imagens JPEG
    for i, image in enumerate(images):
        file_name = os.path.basename(pdf_path)  # Obter o nome do arquivo PDF
        jpeg_path = os.path.join(diretorio_destino, f'{file_name}{i + 1}.jpg');
        image.save(jpeg_path, 'JPEG');
        # Adicionar o caminho do arquivo JPEG à lista
        jpeg_paths.append(jpeg_path);
# Fechar a janela do tkinter
root.destroy();
for jpg in os.listdir("img"):
    imagem = cv2.imread(os.path.join(diretorio_destino,jpg));
    caminho_tesseract = r"C:\Users\itaua\AppData\Local\Programs\Tesseract-ORC"
    pytesseract.pytesseract.tesseract_cmd = os.path.join(caminho_tesseract, 'tesseract.exe')
    # Use o pytesseract para extrair texto da imagem
    texto = pytesseract.image_to_string(imagem);
    # Definir padrão regex para encontrar o valor do documento
    valorDoc = re.compile(r'RS t\s*(\d+,\d+)');
    padrao_nome = re.compile(r'Pagador\s*:\s*([^\-]+)\s*-');
    padrao_cpf = re.compile(r'(\d{3}\.\d{3}\.\d{3}-\d{2})');

    correspondencia = valorDoc.search(texto);
    correspondencia1 = padrao_nome.search(texto);
    correspondencia2 = padrao_cpf.search(texto);

    for pdfR in os.listdir("teste"):
        arquivo_pdf = open(os.path.join("teste", pdfR), 'rb')
        pdf = PyPDF2.PdfReader(arquivo_pdf)
        pagina = pdf.pages[0]
        texto1 = pagina.extract_text()
        corres = re.search(padrao_cpf, texto1)
    
        print (padrao_cpf)
        print (corres)
        if corres:
            print ("O CPF FOI ENCONTRADO NO PDF", pdfR)
        else:
            print("nao foi")

    