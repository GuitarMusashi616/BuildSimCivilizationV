# pyright: strict

from abc import ABC, abstractmethod

from core.Coord import Coord
from tile.ImprovementType import ImprovementType
from tile.ResourceType import ResourceType
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

    @property
    @abstractmethod
    def resource(self) -> ResourceType:
        pass

    def add_yield_change(self, output: TileOutput):
        pass

    @property
    @abstractmethod
    def improvement(self) -> ImprovementType:
        pass
    
    @improvement.setter
    @abstractmethod
    def improvement(self, value: ImprovementType):
        pass
    
