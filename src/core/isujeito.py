from abc import ABC, abstractmethod
from typing import Optional

from src.obsevardores.iobservador import IObservador


class ISujeito(ABC):

    @abstractmethod
    def anexar(self, observador: IObservador):
        pass

    @abstractmethod
    def desanexar(self, observador: IObservador):
        pass

    @abstractmethod
    def notificar(self, dado: Optional[str], flag: int):
        pass
