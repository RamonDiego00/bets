from PIL import Image
import pytesseract
import time

# Capturando texto da imagem

# Caminho para o executável do Tesseract (ajuste conforme necessário)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
""
# Caminho da imagem
caminho_imagem = r'C:\Users\ramon\Downloads\opa.jpeg'

# Abrir a imagem usando a biblioteca PIL
imagem = Image.open(caminho_imagem)

# Extrair o texto usando pytesseract
texto_extraido = pytesseract.image_to_string(imagem)

# Dividir o texto em palavras
palavras = texto_extraido.split()


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
informacoes_extraidas = extrair_informacoes(texto_extraido)

# Imprimindo as informações extraídas
for chave, valor in informacoes_extraidas.items():
    print(f'{chave}: {valor}')


# Imprimir o texto no console
# print(palavras)

# Navegação para o site

from playwright.sync_api import sync_playwright
from unicodedata import name


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