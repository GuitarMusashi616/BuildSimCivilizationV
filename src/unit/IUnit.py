# pyright: strict

from abc import ABC, abstractmethod

from core.Coord import Coord
from unit.IUnitAction import IUnitAction

class IUnit(ABC):
    @property
    @abstractmethod
    def coord(self) -> Coord:
        """Returns the unit's current coordinate location"""
    
    @abstractmethod
    def next_turn(self):
        """Executes a step of the current/next queued action"""
    
    @abstractmethod
    def queue(self, action: IUnitAction):
        """Queues up an action"""
