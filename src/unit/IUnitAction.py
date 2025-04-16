# pyright: strict

from abc import ABC, abstractmethod

from core.Coord import Coord

class IUnitAction(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @property
    @abstractmethod
    def destination(self) -> Coord:
        pass
