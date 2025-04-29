# pyright: strict

from typing import List
from adapter.QueueCityActions import QueueCityActions
from adapter.QueueUnitActions import QueueUnitActions
from building.BuildingDB import BuildingDB
from building.BuildingFactory import BuildingFactory
from core.City import City
from core.Coord import Coord
from map.IMap import IMap
from map.Map import Map
from map.MapFromSave import MapFromSave
from map.MapHelper import MapHelper
from queueable.QueueFactory import QueueFactory
from queueable.QueuedBuildingFactory import QueuedBuildingFactory
from researchable.PolicyFactory import PolicyFactory
from researchable.TechDB import TechDB
from researchable.TechFactory import TechFactory
from src.core.Civ import Civ, Nation
from queueable.QueuedUnitFactory import QueuedUnitFactory
from tile.ITile import ITile
from tile.ImprovementType import ImprovementType
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.Tile import Tile
from unit.ImprovementAction import ImprovementAction
from unit.MoveAction import MoveAction
from unit.SettleAction import SettleAction
from unit.Unit import Unit
from unit.UnitDB import UnitDB
from unit.UnitFactory import UnitFactory

def egypt_turn_0():
    bfactory = BuildingFactory(BuildingDB('resources/Civ5CoreDatabase.db'))
    ufactory = UnitFactory(UnitDB('resources/Civ5CoreDatabase.db'))

    civ = Civ(Nation.EGYPT, bfactory, ufactory)
    civ.add_unit(QueuedUnitFactory.settler().to_unit(Coord(0, 0)))
    civ.add_unit(QueuedUnitFactory.warrior().to_unit(Coord(0, 1)))
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

    bfactory = BuildingFactory(BuildingDB('resources/Civ5CoreDatabase.db'))
    ufactory = UnitFactory(UnitDB('resources/Civ5CoreDatabase.db'))
    civ = Civ(Nation.EGYPT, bfactory, ufactory)

    civ.create_city(base)
    # capital.queue_up(UnitFactory.settler())
    # capital.queue_up(BuildingFactory.granary())

    return civ

def test_lock_hammers_for_extra_hammers_trick():
    """When a city grows it should automatically assign the new population to a tile, if that tile has production then it immediately is added towards the goal"""
    civ = egypt_base_fixture()
    civ.cities[0].queue_up(QueuedBuildingFactory.granary())
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
    civ.cities[0].queue_up(QueuedUnitFactory.settler())
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

    bfactory = BuildingFactory(BuildingDB('resources/Civ5CoreDatabase.db'))
    ufactory = UnitFactory(UnitDB('resources/Civ5CoreDatabase.db'))
    civ = Civ(Nation.EGYPT, bfactory, ufactory)
    capital = civ.create_city(base)
    capital.queue_up(QueuedUnitFactory.settler())

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

    bfactory = BuildingFactory(BuildingDB('resources/Civ5CoreDatabase.db'))
    ufactory = UnitFactory(UnitDB('resources/Civ5CoreDatabase.db'))
    civ = Civ(Nation.EGYPT, bfactory, ufactory)
    capital = civ.create_city(base)
    capital.queue_up(QueuedUnitFactory.settler())

    print("Turn 1")
    civ.stats()
    for i in range(40):
        print(f"Turn {i+2}")
        civ.next_turn()
        civ.stats()
        if len(civ.units) > 0:
            settler = civ.units[0]
            settler.queue(SettleAction(civ, settler.id, MapHelper.get_city_tiles(mapsave, Coord(25, 23))))


def greece():
    policy_order = [
        "POLICY_LIBERTY",
        "POLICY_CITIZENSHIP",
        "POLICY_REPUBLIC",
        "POLICY_COLLECTIVE_RULE",
        "POLICY_REPRESENTATION",
        "POLICY_TRADITION"
    ]

    tech_order = [
        "TECH_POTTERY",
        "TECH_ANIMAL_HUSBANDRY",
        "TECH_MINING",
        "TECH_MASONRY",
        "TECH_TRAPPING"
    ]

    capital_order = [
        "BUILDING_MONUMENT",
        "BUILDING_GRANARY",
        "UNIT_WORKER",
        "UNIT_SCOUT",
        "UNIT_SETTLER",
    ]

    db_path = 'resources/Civ5CoreDatabase.db'
    tfactory = TechFactory(TechDB(db_path))
    bfactory = BuildingFactory(BuildingDB(db_path))
    ufactory = UnitFactory(UnitDB(db_path))
    qfactory = QueueFactory(bfactory, ufactory)

    capital_order = qfactory.from_string_list(capital_order)
    tech_order = tfactory.from_string_list(tech_order)
    policy_order = PolicyFactory.from_string_list(policy_order)

    map = MapFromSave('resources/greece_map.json')
    civ = Civ(Nation.BABYLON, bfactory, ufactory)  # found city turn 1

    start_coord = Coord(20, 29)
    base = MapHelper.get_city_tiles(map, start_coord)

    civ.add_unit_made_listener(QueueUnitActions(0, [SettleAction(civ, 0, base)]))

    civ.add_unit_made_listener(QueueUnitActions(1, [ImprovementAction(civ, 0, 1, Coord(20, 30), 2, ImprovementType.IMPROVEMENT_FARM), MoveAction(start_coord)]))

    civ.add_city_made_listener(QueueCityActions(0, capital_order))

    civ.add_unit(Unit('UNIT_SETTLER', start_coord))

    # MapHelper.find_coord(map, [ResourceType.NONE, ResourceType.RESOURCE_IVORY, ResourceType.NONE, ResourceType.NONE, ResourceType.NONE])

    civ.queue_many_tech(tech_order)
    civ.queue_many_policy(policy_order)


    # coord = Coord(28, 28)

    # capital = civ.create_city(base)
    # capital.queue_up_many(capital_order)

    print("Turn 1")
    civ.stats()
    for i in range(120):
        print(f"Turn {i+2}")
        civ.next_turn()
        civ.stats()


if __name__ == "__main__":
    # test_settler_coord()
    # test_grass_only_map()
    # test_map_from_save()
    # test_settling_map_from_save()
    greece()