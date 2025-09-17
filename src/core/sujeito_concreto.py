from typing import List, Optional

from src.core.isujeito import ISujeito
from ..obsevardores.iobservador import IObservador


class SujeitoConcreto(ISujeito):

    def __init__(self):
        super().__init__()
        self._observadores: List[IObservador] = []

    def anexar(self, observador: IObservador):
        self._observadores.append(observador)

    def remover(self, observador: IObservador):
        self._observadores.remove(observador)

    def notificar(self, dado: Optional[str], flag: int):
        for observador in self._observadores:
            observador.atualizar(dado=dado, flag=flag)

    def desanexar(self, observador: IObservador):
        pass
