# pyright: strict

from abc import ABC, abstractmethod
from typing import Tuple

from core.Coord import Coord
from tile.ITile import ITile

class IMap(ABC):
    @abstractmethod
    def get_tile(self, coord: Coord) -> ITile:
        pass

    @abstractmethod
    def get_width_height(self) -> Tuple[int, int]:
        pass
