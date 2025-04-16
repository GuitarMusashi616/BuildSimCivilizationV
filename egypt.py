from core.Coord import Coord
from queueable.BuildingFactory import BuildingFactory
from src.core.Civ import Civ, Nation
from queueable.WonderFactory import WonderFactory
from test import babylon_race_fixture
from core.City import City
from queueable.UnitFactory import UnitFactory
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.Tile import Tile

def egypt_turn_0():
    civ = Civ(Nation.EGYPT)
    civ.add_unit(UnitFactory.settler())
    civ.add_unit(UnitFactory.warrior())
    return civ


def egypt_base_fixture():
    base = [
        Tile(Coord(1, 1), TerrainType.GRASSLAND_HILL_RIVER),
        Tile(Coord(1, 0), TerrainType.GRASSLAND_RIVER, ResourceType.CATTLE),
        Tile(Coord(2, 0), TerrainType.GRASSLAND_HILL_RIVER, ResourceType.SILVER),

        Tile(Coord(2, 1), TerrainType.COAST),
        Tile(Coord(1, 2), TerrainType.COAST),
        Tile(Coord(0, 1), TerrainType.COAST),

        Tile(Coord(0, 0), TerrainType.GRASSLAND_RIVER),
    ]

    civ = Civ(Nation.EGYPT)

    capital = civ.create_city(base)
    # capital.queue_up(UnitFactory.settler())
    # capital.queue_up(BuildingFactory.granary())

    return civ

def test_lock_hammers_for_extra_hammers_trick():
    """When a city grows it should automatically assign the new population to a tile, if that tile has production then it immediately is added towards the goal"""
    civ = egypt_base_fixture()
    civ.cities[0].queue_up(BuildingFactory.granary())
    print("Turn 1")
    civ.stats()
    for i in range(4):
        print(f"Turn {i+2}")
        civ.next_turn()
        civ.stats()
    city = civ.cities[0]
    assert city.hammers_acc == 22, f"should be 22/60 towards the granary, instead its {city.hammers_acc}/{city.total_hammers_req()}"

def test_settler_coord():
    """Test the new coords for tiles and units"""
    civ = egypt_base_fixture()
    civ.cities[0].queue_up(UnitFactory.settler())
    print("Turn 1")
    civ.stats()
    for i in range(14):
        print(f"Turn {i+2}")
        civ.next_turn()
        civ.stats()
        if len(civ.units) > 0:
            settler = civ.units[0]
            settler.set_destination(Coord(5, 3))
    
    

if __name__ == "__main__":
    # civ = egypt_base_fixture()
    # civ.stats()
    # for i in range(10):
    #     print(f"Turn {i+2}")
    #     civ.next_turn()
    #     civ.stats()
    # print()
    test_settler_coord()