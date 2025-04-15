# pyright: strict

from abc import ABC, abstractmethod

from core.Coord import Coord

class IUnit(ABC):
    @property
    @abstractmethod
    def coord(self) -> Coord:
        pass
    
    @abstractmethod
    def next_turn(self):
        pass