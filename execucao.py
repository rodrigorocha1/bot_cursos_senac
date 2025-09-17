from time import sleep

from src.servico_web_scraping.web_scraping_senac import WebScrapingSenac

wss = WebScrapingSenac()

dados = wss.abrir_dados()


print(wss.consultar_dados_bolsas_estudo(dados=dados))
sleep(5)
print(wss.consultar_dados_cursos_destaque(dados=dados))