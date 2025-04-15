# pyright: strict

from __future__ import annotations
from enum import Enum, auto

from tile.TileOutput import TileOutput

class TerrainType(Enum):

    GRASSLAND = auto()
    GRASSLAND_RIVER = auto()
    GRASSLAND_HILL = auto()
    GRASSLAND_HILL_RIVER = auto()

    PLAINS = auto()
    PLAINS_RIVER = auto()
    PLAINS_HILL = auto()
    PLAINS_HILL_RIVER = auto()

    DESERT = auto()
    DESERT_RIVER = auto()
    DESERT_HILL = auto()
    DESERT_HILL_RIVER = auto()

    TUNDRA = auto()
    TUNDRA_RIVER = auto()
    TUNDRA_HILL = auto()
    TUNDRA_HILL_RIVER = auto()

    COAST = auto()

    @staticmethod
    def base_stats(terrain: TerrainType) -> TileOutput:
        """Return the base stats of food, prod, etc for the terrain eg. grassland hill has 2 hammers"""
        if terrain == TerrainType.GRASSLAND or terrain == TerrainType.GRASSLAND_RIVER or terrain == TerrainType.PLAINS or terrain == TerrainType.PLAINS_RIVER:
            return TileOutput(
                food = 2,
                prod = 0,
                gold = 0,
                culture = 0,
                science = 0,
                faith = 0,
            )
        
        if terrain == TerrainType.GRASSLAND_HILL or terrain == TerrainType.GRASSLAND_HILL_RIVER:
            return TileOutput(
                food = 0,
                prod = 2,
                gold = 0,
                culture = 0,
                science = 0,
                faith = 0,
            )

        assert False, f"Terrain {terrain} has no base stats available"
        
        