# pyright: strict

from core.Coord import Coord
from tile.ITile import ITile
from tile.ImprovementType import ImprovementType
from tile.ResourceType import ResourceType
from tile.TileOutput import TileOutput

class TileString(ITile):
    def __init__(self, coord: Coord, terrain: str, resource: str, improvement: str, is_worked: bool = False, has_city: bool = False):
        self.terrain = terrain
        self.resource = resource
        self.improvement = improvement

        self._coord = coord
        self._is_worked = is_worked
        self._has_city = has_city

    @property
    def is_worked(self) -> bool:
        return self._is_worked

    @is_worked.setter
    def is_worked(self, value: bool):
        self._is_worked = value

    @property
    def has_city(self) -> bool:
        return self._has_city

    @has_city.setter
    def has_city(self, value: bool):
        self._has_city = value

    @property
    def coord(self) -> Coord:
        return self._coord
    
    @property
    def output(self) -> TileOutput:
        return TileOutput(0, 0, 0, 0, 0, 0)
    
    def __repr__(self):
        out =  f"{self.terrain} @ {self.coord}"
        if self.resource != ResourceType.NONE:
            out += f" with {self.resource}"
        if self.improvement != ImprovementType.NONE:
            out += f" and {self.improvement}"
        return out

    