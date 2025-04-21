# pyright: strict

from typing import List
from core.City import City
from core.Coord import Coord
from map.IMap import IMap
from map.Map import Map
from map.MapFromSave import MapFromSave
from map.MapHelper import MapHelper
from queueable.BuildingFactory import BuildingFactory
from src.core.Civ import Civ, Nation
from queueable.UnitFactory import UnitFactory
from tile.ITile import ITile
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.Tile import Tile
from unit.MoveAction import MoveAction
from unit.SettleAction import SettleAction

def egypt_turn_0():
    civ = Civ(Nation.EGYPT)
    civ.add_unit(UnitFactory.settler().to_unit(Coord(0, 0)))
    civ.add_unit(UnitFactory.warrior().to_unit(Coord(0, 1)))
    return civ


def egypt_base_fixture():
    base: List[ITile] = [
        Tile(Coord(1, 1), TerrainType.GRASSLAND_HILL_RIVER),
        Tile(Coord(1, 0), TerrainType.GRASSLAND_RIVER, ResourceType.CATTLE),
        Tile(Coord(2, 0), TerrainType.GRASSLAND_HILL_RIVER, ResourceType.SILVER),

        Tile(Coord(2, 1), TerrainType.COAST),
        Tile(Coord(1, 2), TerrainType.COAST),
        Tile(Coord(0, 1), TerrainType.COAST),

        Tile(Coord(0, 0), TerrainType.GRASSLAND_RIVER),
    ]

    civ = Civ(Nation.EGYPT)

    civ.create_city(base)
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
    assert isinstance(city, City) and city.hammers_acc == 22, f"should be 22/60 towards the granary, instead its {city.hammers_acc}/{city.total_hammers_req()}" # type: ignore

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
            settler.queue(MoveAction(Coord(3, 5)))
    
def test_grass_only_map():
    grassmap = Map.grassmap(-10, 10, 10, -10)
    base = grassmap.get_city_tiles(Coord(0, 0))

    civ = Civ(Nation.EGYPT)
    capital = civ.create_city(base)
    capital.queue_up(UnitFactory.settler())

    print("Turn 1")
    civ.stats()
    for i in range(40):
        print(f"Turn {i+2}")
        civ.next_turn()
        civ.stats()
        if len(civ.units) > 0:
            settler = civ.units[0]
            settler.queue(SettleAction(civ, settler.id, grassmap.get_city_tiles(Coord(5, 0))))


def test_map_from_save():
    # mapsave = MapFromSave('resources/output.json')
    mapsave = MapFromSave('resources/arabia_camel_rush.json')
    width = mapsave.json['MapData']['MapHeader']['Width']
    height = mapsave.json['MapData']['MapHeader']['Height']
    print(width, height)
    for w in range(width):
        for h in range(height):
            print(mapsave.get_tile(Coord(w, h)))

def test_settling_map_from_save():
    mapsave: IMap = MapFromSave('resources/output.json')
    base = MapHelper.get_city_tiles(mapsave, Coord(20, 20))

    civ = Civ(Nation.EGYPT)
    capital = civ.create_city(base)
    capital.queue_up(UnitFactory.settler())

    print("Turn 1")
    civ.stats()
    for i in range(40):
        print(f"Turn {i+2}")
        civ.next_turn()
        civ.stats()
        if len(civ.units) > 0:
            settler = civ.units[0]
            settler.queue(SettleAction(civ, settler.id, MapHelper.get_city_tiles(mapsave, Coord(25, 23))))




if __name__ == "__main__":
    # test_settler_coord()
    # test_grass_only_map()
    # test_map_from_save()
    test_settling_map_from_save()