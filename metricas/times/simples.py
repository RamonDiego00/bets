from playwright.sync_api import sync_playwright


def handicap(time:str, confronto:str):
    return print("")


def escanteio(time: str, confronto: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        def manipular_popups(dialog_info):
            # Rejeitar automaticamente todos os pop-ups
            dialog_info.dismiss()

        page.goto('https://www.365scores.com/pt-br')
        page.on('dialog', manipular_popups)

        search = "xpath=/html/body/div[3]/div/header/div/div/div[1]/div/div[1]/div/div[1]/input"
        cookies = "xpath=//*[@id='didomi-notice-agree-button']"
        resumo = "xpath=/html/body/div[3]/div/main/div[4]/div[1]/div/div[1]/div[2]/div[2]/div/span"
        resultados = "xpath=/html/body/div[3]/div/main/div[4]/div[1]/div/div[1]/div[2]/div[2]/div[2]/span[2]"
        ultimoJogo = "xpath=/html/body/div[3]/div/main/div[4]/div[1]/div/div[2]/div[1]/div[1]/div/div/div/a"
        estatisticas = "xpath=//*[@id='navigation-tabs_game-center_stats']/div"

        # ultimoJogo = "xpath="
        # ultimoJogo = "xpath="
        # ultimoJogo = "xpath="
        # ultimoJogo = "xpath="


        page.fill(search, time)
        page.locator(cookies).click()
        page.wait_for_timeout(2000)
        page.keyboard.press('Enter')
        # page.locator(x).click()
        page.locator(resumo).click()
        page.locator(resultados).click()
        page.locator(ultimoJogo).click()
        page.locator(estatisticas).click()

        #elimina popups
        page.wait_for_timeout(5000)
        page.on('dialog', manipular_popups)
        page.keyboard.press('Escape')

        page.wait_for_timeout(2000)
        direito1 = page.locator("xpath=/html/body/div[3]/div/main/div[4]/div[2]/div[4]/div/div[3]/div/div[2]/div[11]/div/div[1]/div[3]").text_content()
        esquerdo1 = page.locator("xpath=/html/body/div[3]/div/main/div[4]/div[2]/div[4]/div/div[3]/div/div[2]/div[11]/div/div[1]/div[1]").text_content()


        totalPartida1 = int(direito1) + int(esquerdo1)

        #copiar os dados necessarios aqui


        #terminou de copiar os dados de um jogo



        mediaTime = ""
        mediaTotal = ""
        maisEscanteios = ""
        tempoMaisEscanteios = ""

        page.wait_for_timeout(2000)
        browser.close()

    return print(f"Nas ultimas 10 partidas o {time} fez uma média de {totalPartida1} escanteios,"
                 f" a média total dos times nesses em 10 jogos é {mediaTotal},"
                 f" Nos ultimos 10 jogos fez mais escantios em {maisEscanteios} jogos,"
                 f" mais escanteios no {tempoMaisEscanteios}° tempo,"
                 f""
                 f""
                 f"   ")


def resultado(time: str, confronto: str):
    return print()


def ambasMarcam(time: str, confronto: str):
    return print()


def cartoes(time: str, confronto: str):
    return print()


def golsPartida(time: str, confronto: str):
    return print()
