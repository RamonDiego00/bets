import time
from PIL import Image

import cv2
import pytesseract

def extrair_paragrafos():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Carregue a imagem
    imagem = cv2.imread(r'C:\Users\ramon\Downloads\teste1.jpeg', cv2.IMREAD_GRAYSCALE)

    # Aplique binarização para segmentar linhas
    _, binarizada = cv2.threshold(imagem, 128, 255, cv2.THRESH_BINARY_INV)

    # Use pytesseract para obter informações sobre os espaçamentos
    info_linhas = pytesseract.image_to_boxes(binarizada)

    # Inicialize variáveis
    paragrafos = []
    paragrafo_atual = ""
    espaco_limite = 1  # Ajuste conforme necessário
    primeiro_paragrafo = True

    # Analise o espaçamento vertical entre as linhas
    for linha_info in info_linhas.splitlines():
        valores = linha_info.split()

        # Verifique se há informações suficientes para o desempacotamento
        if len(valores) >= 7:
            _, _, _, _, y_max, _, _ = map(int, valores[4:11])

            # Se o espaçamento vertical for maior que o limite, adicione o parágrafo à lista
            if y_max > espaco_limite:
                if not primeiro_paragrafo:
                    paragrafos.append(paragrafo_atual.strip())
                else:
                    primeiro_paragrafo = False
                # Reinicie o parágrafo atual
                paragrafo_atual = ""
            else:
                # Adicione a linha ao parágrafo atual
                paragrafo_atual += valores[11]

    # Adicione o último parágrafo à lista
    paragrafos.append(paragrafo_atual.strip())

    # Imprima os parágrafos em ordem numerada
    for i, paragrafo in enumerate(paragrafos, start=1):
        print(f"Parágrafo {i}:\n{paragrafo}\n")



def copiando():

    extrair_paragrafos()

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