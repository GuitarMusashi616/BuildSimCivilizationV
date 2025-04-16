# pyright: strict

from abc import ABC, abstractmethod

from core.Coord import Coord

class IUnit(ABC):
    @property
    @abstractmethod
    def coord(self) -> Coord:
        """Returns the unit's current coordinate location"""
    
    @abstractmethod
    def next_turn(self):
        """Executes the next queued action"""

    @abstractmethod
    def set_destination(self, coord: Coord):
        """Unit starts moving towards coord every turn until it arrives"""