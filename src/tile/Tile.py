# pyright: strict

from core.Coord import Coord
from tile.ITile import ITile
from tile.ImprovementType import ImprovementType
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.TileOutput import TileOutput

class Tile(ITile):
    def __init__(self, coord: Coord, terrain: TerrainType, resource: ResourceType = ResourceType.NONE, improvement: ImprovementType = ImprovementType.NONE, is_worked: bool = False, has_city: bool = False):
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
        output = TerrainType.base_stats(self.terrain)
        output += ResourceType.add_stats(self.resource)
        if self.has_city:
            output = output.set_minimum(TileOutput.minimum_if_tile_has_city())
        return output

    