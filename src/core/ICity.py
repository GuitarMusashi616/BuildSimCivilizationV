# pyright: strict

from abc import ABC, abstractmethod
from typing import List

from core.Coord import Coord
from queueable.IQueue import IQueue
from tile.ITile import ITile

class ICity(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        """Returns the entity's id"""

    @property
    @abstractmethod
    def tiles(self) -> List[ITile]:
        """Returns the tiles that the city is on"""

    @abstractmethod
    def next_turn(self):
        """Simulates the next turn of the city"""

    @abstractmethod
    def stats(self):
        """Prints the status of the city"""

    @abstractmethod
    def queue_up(self, iqueue: IQueue):
        pass

    @abstractmethod
    def queue_up_many(self, queue: List[IQueue]):
        pass
    
    @abstractmethod
    def get_gold(self) -> int:
        pass

    @abstractmethod
    def get_pop(self) -> int:
        pass

    @abstractmethod
    def get_science(self) -> int:
        pass

    @abstractmethod
    def get_culture(self) -> int:
        pass

    @abstractmethod
    def get_faith(self) -> int:
        pass
    
    @abstractmethod
    def get_tile(self, coord: Coord) -> ITile:
        pass

