from abc import abstractmethod, ABC
from typing import TypeVar, Generic, List, Dict

T = TypeVar('T')


class IWebScrapingSenac(ABC, Generic[T]):

    @abstractmethod
    def abrir_dados(self) -> T:
        pass

    @abstractmethod
    def consultar_dados_bolsas_estudo(self, dados: T) -> List[Dict[str, str]]:
        pass

    @abstractmethod
    def consultar_dados_cursos_destaque(self, dados: T) -> List[Dict[str, str]]:
        pass

    @abstractmethod
    def consultar_dados_cursos_proximas_turmas(self, dados: T) -> List[Dict[str, str]]:
        pass
