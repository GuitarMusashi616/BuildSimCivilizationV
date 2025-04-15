# pyright: strict

from abc import ABC, abstractmethod

from core.Coord import Coord
from tile.TileOutput import TileOutput

class ITile(ABC):
    @property
    @abstractmethod
    def is_worked(self) -> bool:
        pass

    @is_worked.setter
    @abstractmethod
    def is_worked(self, value: bool):
        pass

    @property
    @abstractmethod
    def has_city(self) -> bool:
        pass

    @has_city.setter
    @abstractmethod
    def has_city(self, value: bool):
        pass

    @property
    @abstractmethod
    def coord(self) -> Coord:
        pass

    @property
    @abstractmethod
    def output(self) -> TileOutput:
        pass
    
