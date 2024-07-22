# pyright: strict

import abc
from typing import List
from tile.Tile import Tile

class IPickTileStrat(abc.ABC):
    @abc.abstractmethod
    def pick_tiles(self, tiles: List[Tile], how_many: int) -> List[int]:
        """Given the tiles that make up the city and how many citizens to work, return the indices of the tiles to work"""