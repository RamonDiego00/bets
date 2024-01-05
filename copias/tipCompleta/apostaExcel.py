import datetime
import random
import os.path
import pytesseract
import tkinter as tk
from PIL import Image
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tkinter import filedialog

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1KyZhn9tXtMfHNf76fe0RP0c19c9iwEzLtkKXW6LsptU"
SAMPLE_RANGE_NAME = "Janeiro!A2:E"

# Interface visual

def selecionar_imagens():
    # Abre uma janela de seleção de arquivos
    arquivos = filedialog.askopenfilenames(
        title="Selecionar Imagens",
        filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.gif")]
    )

    # Exibe os caminhos dos arquivos selecionados
    for arquivo in arquivos:
        planilha(arquivo)


def abrindo_janela():
    root = tk.Tk()
    # Cria um botão para selecionar imagens
    botao_selecionar = tk.Button(root, text="Selecionar Imagens", command=selecionar_imagens)
    botao_selecionar.pack(pady=20)
    # Exibe a janela
    root.mainloop()


#código antigo

def encontrar_valores(palavras):
    # Encontrar o índice onde começa a seção de Aposta Retornos
    indice_retornos = encontrar_indice_retornos(palavras)

    # Inicializar variáveis
    valor_retorno = 0
    valor_apostado = 0
    resolvida = False

    if indice_retornos != -1:
        # Encontrar o valor do retorno (duas posições à frente)
        indice_valor_retorno = indice_retornos + 2
        if indice_valor_retorno < len(palavras):
            valor_retorno_str = palavras[indice_valor_retorno].replace('R$', '').replace(',', '.')
            if 'O' in valor_retorno_str:
                valor_retorno = 0.00
            else:
                valor_retorno = float(valor_retorno_str)
        # Encontrar o valor apostado (uma posição à frente)
        indice_apostado = indice_retornos + 1
        if indice_apostado < len(palavras):
            valor_apostado_str = palavras[indice_apostado].replace('R$', '').replace(',', '.')
            valor_apostado = float(valor_apostado_str)

        if valor_retorno != 0:
            resolvida = True
        else:
            resolvida = False

    return valor_retorno, valor_apostado, resolvida



def encontrar_indice_retornos(palavras):
    try:
        indice_retornos = palavras.index('Retornos')
        return indice_retornos
    except ValueError:
        try:
            indice_retornos = palavras.index('Retorno')
            return indice_retornos + 1
        except ValueError:
            try:
                indice_total = palavras.index('Total')
                return indice_total
            except ValueError:
                return -1

def planilha(nome):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

            # Capturando texto da imagem

            # Caminho para o executável do Tesseract (ajuste conforme necessário)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ""
    # Caminho da imagem
    caminho_imagem = nome

    # Abrir a imagem usando a biblioteca PIL
    imagem = Image.open(caminho_imagem)

    # Extrair o texto usando pytesseract
    texto_extraido = pytesseract.image_to_string(imagem)

    # Dividir o texto em palavras
    palavras = texto_extraido.split()
    print(palavras)

    # nova_linha = ["1", "True", "20", "29/12/2023", "Indefinido", "1000"]
    id_unico = random.randint(1000, 9999)

    # Gera a data atual
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y")

    # Define os dados a serem adicionados
    linha = list(encontrar_valores(palavras))
    linha.insert(0, linha.pop(2))
    linha.insert(0, id_unico)
    linha.insert(3, data_atual)
    linha.insert(4, "Indefinido")

    # nova_linha = [str(id_unico), "True", "8118.0", data_atual, "Chute a gol", "apostado"]
    nova_linha = linha
    try:
        service = build("sheets", "v4", credentials=creds)

        # Obtém a instância da planilha
        sheet = service.spreadsheets()

        # Obtém os valores existentes na planilha
        result = (
            sheet.values()
                .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
                .execute()
        )
        values = result.get("values", [])

        # Adiciona uma nova linha com os dados fornecidos
        nova_linha_range = f"Janeiro!A{len(values) + 2}:F{len(values) + 2}"
        nova_linha_body = {"values": [nova_linha]}
        sheet.values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=nova_linha_range,
            body=nova_linha_body,
            valueInputOption="RAW",
        ).execute()

        print("Nova linha adicionada com sucesso.")

    except HttpError as err:
        print(err)
