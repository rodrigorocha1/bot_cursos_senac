from abc import ABC, abstractmethod
from typing import Optional


class IObservador(ABC):

    @abstractmethod
    def atualizar(self, dado: Optional[str], flag: int):
        pass
