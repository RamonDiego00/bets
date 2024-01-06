import time
from PIL import Image
import pytesseract
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\tips\credentials.json"
from google.oauth2 import service_account
from google.cloud import vision_v1
from google.protobuf.json_format import MessageToJson

import cv2
import pytesseract

import cv2
import pytesseract

import cv2
import pytesseract

import cv2
import pytesseract

def identify_phrases(image_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Importar a imagem
    image = cv2.imread(image_path)

    # Converter a imagem para escala de cinza
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar thresholding na imagem
    thresholded_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY_INV)[1]

    # Encontrar apenas contornos maiores
    contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]

    # Iterar sobre os contornos maiores
    phrases = []
    current_phrase = ""

    for contour in large_contours:
        # Encontrar a caixa delimitadora do contorno
        x, y, w, h = cv2.boundingRect(contour)

        # Verificar se a caixa delimitadora é grande o suficiente
        if w > 10 and h > 10:
            # Extrair o texto da caixa delimitadora
            text = pytesseract.image_to_string(image[y:y + h, x:x + w])

            # Adicionar o texto à frase atual
            current_phrase += text

            # Verificar se o texto contém um ponto
            if "." in text:
                # A frase terminou, adicionar à lista de frases
                phrases.append(current_phrase.strip())
                # Imprimir a frase no console
                print(current_phrase.strip())
                # Iniciar uma nova frase
                current_phrase = ""

    # Adicionar a última frase, se houver
    if current_phrase:
        phrases.append(current_phrase.strip())
        # Imprimir a última frase no console
        print(current_phrase.strip())
    else:
        # Se nenhuma frase foi encontrada, imprimir a mensagem "nada encontrado"
        print("nada encontrado")

    return phrases





def detect_text(image_path):
    # Caminho para o arquivo de credenciais JSON
    credentials_path = 'C:/tips/credentials.json'

    # Carregue as credenciais do arquivo JSON
    credentials = service_account.Credentials.from_service_account_file(credentials_path)

    # Use as credenciais ao criar o cliente Vision
    client = vision_v1.ImageAnnotatorClient(credentials=credentials)

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        for text in texts:
            print(f'Detected text: "{text.description}"')
            vertices = [(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices]
            print(f'Bounding Polygon: {vertices}')

            # Converte as informações para JSON para análise adicional se necessário
            text_json = MessageToJson(text)
            print(f'Text JSON: {text_json}')
    else:
        print('No text detected.')









def copiando():

    # extrair_paragrafos()

    # Caminho da imagem

    # Capturando texto da imagem

    # Caminho para o executável do Tesseract (ajuste conforme necessário)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ""
    # Caminho da imagem
    caminho_imagem = r'C:\Users\ramon\Downloads\teste1.jpeg'

    # Abrir a imagem usando a biblioteca PIL
    imagem = Image.open(caminho_imagem)

    # Extrair o texto usando pytesseract
    texto_extraido = pytesseract.image_to_string(imagem)

    # Dividir o texto em palavras
    palavras = texto_extraido.split()

    print(palavras)

    #Vamos mudar a estrategia, pegar o index de criar(começo) e pegar o index de valor(final)
    try:
        indice_criar = palavras.index('Criar')
        print(indice_criar)
    except ValueError:
        indice_criar = -1
    try:
        indice_valor = palavras.index('Valor')
        print(indice_valor)
    except ValueError:
        indice_total = 1


    #pegar confronto
    confronto = ' '.join(palavras[11:14])
    print(confronto)
    #Separar em container cada aposta das multiplas




    #fazer tratamento para cada tipo de aposta(Time/jogador)


    #Time  cartão
    #Time gols (mais ou menos gols)
    #Time resultado


def extrair_informacoes(lista):




    informacoes = {}
    encontrou_numero = False
    entre_tracos = False
    chave_atual = None
    jogo_atual = []

    for palavra in lista:
        if palavra == '-':
            if not entre_tracos:
                entre_tracos = True
                chave_atual = None
                if jogo_atual:
                    informacoes['jogo'] = ' '.join(jogo_atual)
                    jogo_atual = []
        elif entre_tracos:
            if chave_atual is None:
                chave_atual = palavra
            else:
                chave_atual += ' ' + palavra

            if encontrou_numero and not chave_atual.startswith('-'):
                informacoes[chave_atual] = palavra
                encontrou_numero = False
            elif palavra.replace('.', '', 1).isdigit() and '.' in palavra:
                encontrou_numero = True
            elif chave_atual == 'jogo':
                jogo_atual.append(palavra)

    return informacoes


# Extraindo informações
# informacoes_extraidas = extrair_informacoes(texto_extraido)

# Imprimindo as informações extraídas
# for chave, valor in informacoes_extraidas.items():
#     print(f'{chave}: {valor}')


# Imprimir o texto no console
# print(palavras)

# Navegação para o site

from playwright.sync_api import sync_playwright


def example_playwright_automation():
    with sync_playwright() as p:
        # Iniciar o navegador (pode ser 'chromium', 'firefox' ou 'webkit')
        browser = p.chromium.launch(headless=False)

        # Criar uma nova página
        page = browser.new_page()

        # Navegar para o Google
        page.goto('https://www.bet365.com/?affiliate=365_02667223&gclid=CjwKCAiA-P-rBhBEEiwAQEXhH-yTmRmIswHFrrieagZfBLQuaDedy4o-CfwzInwWB-hIKbTjqpeg8BoCfaMQAvD_BwE#/AC/B18/C20915116/D48/E1453/F10/')

        page.wait_for_timeout(2000)
        # page.locator('xpath=/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[4]/div[2]/div').click()
        page.locator("xpath=/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[4]/div[2]/div").click()
        page.wait_for_timeout(2000)
        page.fill("xpath=/html/body/div[1]/div/div[3]/div/div[2]/input", "Ramonzin35")
        page.fill("xpath=/html/body/div[1]/div/div[3]/div/div[3]/input", "ApostasBrabas980#")
        page.locator("xpath=/html/body/div[1]/div/div[3]/div/div[4]/div").click()
        time.sleep(10)
        page.locator("xpath=/html/body/div[1]/div/div[3]/div[1]/div/div[3]/div[4]/div[1]/div").click()
        page.locator("xpath=/html/body/div[1]/div/div[3]/div[1]/div/div[3]/div[2]/div[1]/input").click()

        # Vamos colocar a pesquisa do jogo aqui
        page.fill("xpath=/html/body/div[1]/div/div[3]/div/div[3]/input", "ApostasBrabas980#")
        # Fechar o navegador
        browser.close()

# example_playwright_automation()

# Uma função com nome, senha,imagem, valor


# Aqui são as chamadas regulares

# times.resultado("Real Madrid","Real Madrid vs Alaves")