# pyright: strict

from tile.ImprovementType import ImprovementType
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.Tile import Tile


class TileFactory:
    @staticmethod
    def grassland() -> Tile:
        return Tile(TerrainType.GRASSLAND, ResourceType.NONE, ImprovementType.NONE)
    
    @staticmethod
    def grassland_hill() -> Tile:
        return Tile(TerrainType.GRASSLAND_HILL, ResourceType.NONE, ImprovementType.NONE)

    @staticmethod
    def grassland_hill_river() -> Tile:
        return Tile(TerrainType.GRASSLAND_HILL_RIVER, ResourceType.NONE, ImprovementType.NONE)

    @staticmethod
    def grassland_hill_river_city() -> Tile:
        return Tile(TerrainType.GRASSLAND_HILL_RIVER, ResourceType.NONE, ImprovementType.NONE)
    
    @staticmethod
    def grassland_river() -> Tile:
        return Tile(TerrainType.GRASSLAND_RIVER, ResourceType.NONE, ImprovementType.NONE)

    @staticmethod
    def grassland_river_city() -> Tile:
        return Tile(TerrainType.GRASSLAND_RIVER, ResourceType.NONE, ImprovementType.NONE)

    @staticmethod
    def grassland_river_stone() -> Tile:
        return Tile(TerrainType.GRASSLAND, ResourceType.STONE, ImprovementType.NONE)
    
    @staticmethod
    def forest_grassland() -> Tile:
        return Tile(TerrainType.GRASSLAND, ResourceType.NONE, ImprovementType.NONE)
    
    @staticmethod
    def plains_river() -> Tile:
        return Tile(TerrainType.PLAINS, ResourceType.NONE, ImprovementType.NONE)