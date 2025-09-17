import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

from src.config.config import Config
from src.obsevardores.iobservador import IObservador


class ObservadorGmailEmail(IObservador):
    def __init__(self, assunto: str):
        self.__remetente = Config.EMAIL_REMENTENTE
        self.__destinatario = Config.EMAIL_DESTINATARIO
        self.__senha = Config.SENHA_EMAIL
        self.__mensagem = MIMEMultipart()
        self.__assunto = assunto
        self.__servico_email = smtplib.SMTP('smtp.gmail.com: 587')

    def __preparar_dados(self, dados: str):
        mensagem = MIMEMultipart()
        mensagem['Subject'] = self.__assunto
        mensagem['From'] = self.__remetente
        mensagem['To'] = self.__destinatario
        corpo = MIMEText(dados, 'html')
        mensagem.attach(corpo)
        return mensagem

    def __enviar_dados(self, mensagem):
        with smtplib.SMTP('smtp.gmail.com', 587) as servico_email:
            servico_email.ehlo()
            servico_email.starttls()
            servico_email.login(self.__remetente, self.__senha)
            servico_email.sendmail(
                self.__remetente,
                [self.__destinatario],
                mensagem.as_string()
            )

    def atualizar(self, dados: Optional[str], flag: int):
            if flag == 2:

                mensagem = self.__preparar_dados(dados=dados)
                self.__enviar_dados(mensagem=mensagem)
