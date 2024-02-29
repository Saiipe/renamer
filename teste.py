import cv2
import pytesseract

# Variáveis globais para armazenar coordenadas de cliques
x1, y1, x2, y2 = -1, -1, -1, -1
cropping = False

def cortar_imagem(event, x, y, flags, param):
    global x1, y1, x2, y2, cropping

    # Se o botão esquerdo do mouse for pressionado, iniciar o recorte
    if event == cv2.EVENT_LBUTTONDOWN:
        x1, y1, x2, y2 = x, y, x, y
        cropping = True

    # Atualizar as coordenadas do retângulo à medida que o mouse se move
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            x2, y2 = x, y

    # Se o botão esquerdo do mouse for liberado, finalizar o recorte
    elif event == cv2.EVENT_LBUTTONUP:
        x2, y2 = x, y
        cropping = False

        # Desenhar o retângulo na imagem
        cv2.rectangle(imagem, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.imshow('Imagem', imagem)

        # Cortar e mostrar a região selecionada
        regiao_cortada = imagem[min(y1,y2):max(y1,y2), min(x1,x2):max(x1,x2)]

        # Converter a região cortada em texto usando OCR
        texto = pytesseract.image_to_string(regiao_cortada)

        # Exibir o texto extraído
        print("Texto extraído:", texto)
        
        # Aguardar um momento para que o usuário veja o resultado antes de fechar as janelas
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Carregar a imagem
imagem = cv2.imread('img/pagina_1_danfe.pdf.jpg')

# Clonar a imagem para desenhar o retângulo sem alterar a original
clone = imagem.copy()

# Criar a janela e definir a função de callback do mouse
cv2.namedWindow('Imagem')
cv2.setMouseCallback('Imagem', cortar_imagem)

while True:
    # Exibir a imagem com o retângulo desenhado
    cv2.imshow('Imagem', imagem)

    # Se a tecla 'r' for pressionada, resetar a imagem para o estado original
    if cv2.waitKey(1) & 0xFF == ord('r'):
        imagem = clone.copy()

    # Se a tecla 'c' for pressionada, sair do loop
    elif cv2.waitKey(1) & 0xFF == ord('c'):
        break

# Fechar todas as janelas
cv2.destroyAllWindows()
