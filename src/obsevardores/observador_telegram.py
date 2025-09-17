from typing import Optional

from telebot import TeleBot

from .iobservador import IObservador
from ..config.config import Config


class ObservadorTelegram(IObservador):

    def __init__(self):
        self.__TOKEN_TELEGRAM = Config.TOKEN_TELEGRAM
        self.__CHAT_ID = Config.CHAT_ID
        self.__bot = TeleBot(self.__TOKEN_TELEGRAM)

    def atualizar(self, dado: Optional[str], flag: int):
        if flag == 1:
            self.__bot.send_message(self.__CHAT_ID, dado, parse_mode="HTML")
