from src.core.Civ import Civ, Nation
from queueable.WonderFactory import WonderFactory
from test import babylon_race_fixture
from core.City import City
from queueable.UnitFactory import UnitFactory
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.Tile import Tile
from tile.TileFactory import TileFactory

def egypt_turn_0():
    civ = Civ(Nation.EGYPT)
    civ.add_unit(UnitFactory.settler(), 0)
    civ.add_unit(UnitFactory.warrior(), 1)
    return civ


def egypt_base_fixture():
    base = [
        Tile(TerrainType.GRASSLAND_HILL_RIVER),
        Tile(TerrainType.GRASSLAND_RIVER, ResourceType.CATTLE),
        Tile(TerrainType.GRASSLAND_HILL_RIVER, ResourceType.SILVER),

        Tile(TerrainType.COAST),
        Tile(TerrainType.COAST),
        Tile(TerrainType.COAST),

        Tile(TerrainType.GRASSLAND_RIVER),
    ]

    civ = Civ(Nation.EGYPT)

    capital = City(base)

    capital.add_wonder(WonderFactory.palace())
    capital.pick_tiles_with_strat()

    civ.add_city(capital, 0)

    return civ

if __name__ == "__main__":
    civ = egypt_turn_0()
    civ.stats()