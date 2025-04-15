from queueable.BuildingFactory import BuildingFactory
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
    capital.queue_up(BuildingFactory.granary())

    civ.add_city(capital, 0)

    return civ

def test_lock_hammers_for_extra_hammers_trick():
    """When a city grows it should automatically assign the new population to a tile, if that tile has production then it immediately is added towards the goal"""
    civ = egypt_base_fixture()
    print("Turn 1")
    civ.stats()
    for i in range(4):
        print(f"Turn {i+2}")
        civ.next_turn()
        civ.stats()
    city = civ.cities[0]
    assert city.hammers_acc == 22, f"should be 22/60 towards the granary, instead its {city.hammers_acc}/{city.total_hammers_req()}"
    

if __name__ == "__main__":
    # civ = egypt_base_fixture()
    # civ.stats()
    # for i in range(10):
    #     print(f"Turn {i+2}")
    #     civ.next_turn()
    #     civ.stats()
    # print()
    test_lock_hammers_for_extra_hammers_trick()