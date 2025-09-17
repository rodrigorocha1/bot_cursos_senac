from time import sleep
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from src.servico_web_scraping.i_web_scraping_senac import IWebScrapingSenac


class WebScrapingSenac(IWebScrapingSenac[WebDriver]):

    def __init__(self):
        self.__url = 'https://www.sp.senac.br/senac-ribeirao-preto'
        self.__servico = Service(ChromeDriverManager().install())
        self.__opcao = webdriver.ChromeOptions()
        self.__opcao.add_argument("--start-maximized")

    def abrir_dados(self) -> WebDriver:
        navegador = webdriver.Chrome(service=self.__servico, options=self.__opcao)
        navegador.get(url=self.__url)
        return navegador

    def __mover_slider_curso_bolsa_estudo(self, dados: WebDriver):
        elemento = dados.find_element(
            By.ID, "slider-cursos-bolsa")
        dados.execute_script("arguments[0].scrollIntoView();", elemento)
        sleep(4)

    def __executar_paginacao_bolsa_estudo(self, dados: WebDriver) -> bool:
        dados_navegador = dados.find_element(
            By.CLASS_NAME, "slick-next").get_attribute("aria-disabled")
        dados.find_element(By.CLASS_NAME, "slick-next").click()
        flag = False if dados_navegador == 'true' else True
        return flag

    def consultar_dados_bolsas_estudo(self, dados: WebDriver) -> List[Dict[str, str]]:
        self.__mover_slider_curso_bolsa_estudo(dados=dados)

        lista_cursos = []
        cursos_com_bolsas = dados.find_element(By.CLASS_NAME, "slick-track")
        cursos_com_bolsas = cursos_com_bolsas.find_elements(By.CLASS_NAME, "slick-area__item")
        flag = True
        while flag:

            for curso in cursos_com_bolsas:
                if curso.find_element(By.TAG_NAME, "h6").text.strip():
                    lista_cursos.append(
                        {
                            'nome_curso': curso.find_element(By.TAG_NAME, "h6").text.strip(),
                            'url_curso': curso.find_element(
                                By.CLASS_NAME, "text-decoration-none").get_attribute("href")
                        }
                    )
            flag = self.__executar_paginacao_bolsa_estudo(dados)
            print(flag)
        return lista_cursos

    def mover_slide_cursos_destaque(self, dados: WebDriver) -> bool:
        pass

    def executar_paginacao_cursos_destaque(self, dados: WebDriver):
        pass

    def consultar_dados_cursos_destaque(self, dados: WebDriver) -> List[Dict[str, str]]:
        pass

    def mover_slide_cursos_proximas_turmas(self, dados: WebDriver) -> bool:
        pass

    def executar_paginacao_cursos_proximas_turmas(self, dados: WebDriver):
        pass

    def consultar_dados_cursos_proximas_turmas(self, dados: WebDriver) -> List[Dict[str, str]]:
        pass
