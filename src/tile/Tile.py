# pyright: strict

from tile.ImprovementType import ImprovementType
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.TileOutput import TileOutput

class Tile:
    def __init__(self, terrain: TerrainType, resource: ResourceType, improvement: ImprovementType, is_worked: bool = False):
        self.terrain = terrain
        self.resource = resource
        self.improvement = improvement
        self.is_worked = is_worked

    @property
    def output(self) -> TileOutput:
        return TerrainType.base_stats(self.terrain)

    