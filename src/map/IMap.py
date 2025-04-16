# pyright: strict

from abc import ABC, abstractmethod

from core.Coord import Coord
from tile.ITile import ITile

class IMap(ABC):
    @abstractmethod
    def get_tile(self, coord: Coord) -> ITile:
        pass