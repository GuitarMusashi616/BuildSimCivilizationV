# pyright: strict

from typing import List
from adapter.QueueUnitActions import QueueUnitActions
from building.BuildingDB import BuildingDB
from building.BuildingFactory import BuildingFactory
from core.Civ import Civ
from core.Coord import Coord
from enums.Nation import Nation
from map.MapHelper import MapHelper
from queueable.QueueFactory import QueueFactory
from queueable.QueuedBuildingFactory import QueuedBuildingFactory
from queueable.IQueue import IQueue
from queueable.QueuedUnitFactoryStandard import QueuedUnitFactoryStandard
from researchable.PolicyFactory import PolicyFactory
from researchable.Tech import Tech
from researchable.Policy import Policy
from queueable.QueuedUnitFactory import QueuedUnitFactory
from researchable.TechDB import TechDB
from researchable.TechFactory import TechFactory
from tile.ITile import ITile
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.Tile import Tile
from map.MapFromSave import MapFromSave
from unit.IUnitAction import IUnitAction
from unit.SettleAction import SettleAction
from unit.UnitDB import UnitDB
from unit.UnitFactory import UnitFactory

def get_base() -> List[ITile]:
    base: List[ITile] = [
        Tile(Coord(1, 1), TerrainType.GRASSLAND_RIVER),
        Tile(Coord(1, 0), TerrainType.GRASSLAND_HILL),
        Tile(Coord(2, 0), TerrainType.FOREST_GRASSLAND),
        Tile(Coord(2, 1), TerrainType.GRASSLAND_RIVER),
        Tile(Coord(1, 2), TerrainType.GRASSLAND_RIVER),
        Tile(Coord(0, 1), TerrainType.PLAINS_RIVER),
        Tile(Coord(0, 0), TerrainType.GRASSLAND_RIVER, ResourceType.STONE),

        Tile(Coord(2, 2), TerrainType.GRASSLAND_RIVER),
        Tile(Coord(2, 1), TerrainType.GRASSLAND_HILL),
        Tile(Coord(3, 1), TerrainType.FOREST_GRASSLAND),
        Tile(Coord(3, 2), TerrainType.GRASSLAND_RIVER),
        Tile(Coord(2, 3), TerrainType.GRASSLAND_RIVER),
        Tile(Coord(1, 2), TerrainType.PLAINS_RIVER),
        Tile(Coord(1, 1), TerrainType.GRASSLAND_RIVER, ResourceType.STONE),
    ]
    return base




def main():
    # first tile is the city
    # then start above it going clockwise (start on upper right if two tiles above first tile)
    bfactory = BuildingFactory(BuildingDB('resources/Civ5CoreDatabase.db'))
    ufactory = UnitFactory(UnitDB('resources/Civ5CoreDatabase.db'))

    civ = Civ(Nation.ARABIA, bfactory, ufactory)

    capital = civ.create_city(get_base())
    capital.queue_up(QueuedUnitFactory.worker())

    civ.queue_tech(Tech('Pottery', 25))
    civ.queue_policy(Policy('Oligarchy')) # type: ignore
    civ.stats()

    for i in range(2, 20):
        civ.next_turn()
        print(f"TURN {i}")
        print()
        civ.stats()


def test_arabia_camel_archer_rush():
    build_order_tech = [
        Tech('Pottery', 35),
        Tech('Animal Husbandry', 35),
        Tech('Mining', 35),
        Tech('Calendar', 55),  # specific luxury resource tech for grapes
        Tech('Writing', 55),
        Tech('Archery', 35),
        Tech('Wheel', 55),
        Tech('Mathematics', 105),
        Tech('Drama & Poetry', 175),
        Tech('Trapping', 55),
        Tech('Horseback Riding', 105),
        Tech('Currency', 175),
        Tech('Civil Service', 275),
        Tech('Chivalry', 485),
    ]

    build_order_policy = [
        Policy('Republic'),
        Policy('Collective Rule'),
        Policy('Citizenship'),
        Policy('Representation'),
        Policy('Meritocracy')
    ]

    build_order_capital: List[IQueue] = [
        QueuedUnitFactoryStandard.scout(),
        QueuedUnitFactoryStandard.scout(),
        QueuedBuildingFactory.granary(),
        QueuedUnitFactoryStandard.scout(),
        QueuedUnitFactoryStandard.settler(),
        QueuedUnitFactoryStandard.settler(),
    ]

    build_order_expansions: List[IQueue] = [ # type: ignore
        QueuedBuildingFactory.granary(),
        QueuedBuildingFactory.library(),
        QueuedUnitFactoryStandard.chariot(),
    ]


    map = MapFromSave('resources/arabia_camel_rush.json')

    ufactory = UnitFactory(UnitDB('resources/Civ5CoreDatabase.db'))
    bfactory = BuildingFactory(BuildingDB('resources/Civ5CoreDatabase.db'))

    civ = Civ(Nation.BABYLON, bfactory, ufactory)  # found city turn 1

    capital = civ.create_city(MapHelper.get_city_tiles(map, Coord(36, 20)))
    capital.queue_up_many(build_order_capital)
    civ.queue_many_tech(build_order_tech)
    civ.queue_many_policy(build_order_policy)

    # settler_count = 0
    # settle_coords = [Coord(36, 28), Coord(28, 28), Coord(23, 23), Coord(20, 20), Coord(15, 15)]

    first_actions: List[IUnitAction] = [SettleAction(civ, 3, MapHelper.get_city_tiles(map, Coord(36, 28)))]
    civ.add_unit_made_listener(QueueUnitActions(3, first_actions))

    second_actions: List[IUnitAction] = [SettleAction(civ, 4, MapHelper.get_city_tiles(map, Coord(28, 28)))]
    civ.add_unit_made_listener(QueueUnitActions(4, second_actions))

    print("Turn 1")
    civ.stats()
    for i in range(120):
        print(f"Turn {i+2}")
        civ.next_turn()
        civ.stats()

    return civ


def babylon_archer_rush():
    build_order_tech = [
        Tech('Archery', 35),
        Tech('Pottery', 35),
        Tech('Writing', 55),
        Tech('Mining', 35),
        Tech('Bronze Working', 35),
        Tech('Iron Working', 35),
        Tech('Animal Husbandry', 35),
        Tech('Calendar', 55),  # specific luxury resource tech for grapes
        Tech('Wheel', 55),
        Tech('Mathematics', 105),
        Tech('Drama & Poetry', 175),
        Tech('Trapping', 55),
        Tech('Horseback Riding', 105),
        Tech('Currency', 175),
        Tech('Civil Service', 275),
        Tech('Chivalry', 485),
    ]

    build_order_policy = [
        Policy('Republic'),
        Policy('Collective Rule'),
        Policy('Citizenship'),
        Policy('Representation'),
        Policy('Meritocracy')
    ]

    build_order_capital: List[IQueue] = [
        QueuedUnitFactoryStandard.scout(),
        QueuedUnitFactoryStandard.scout(),
        QueuedBuildingFactory.granary(),
        QueuedUnitFactoryStandard.scout(),
        QueuedUnitFactoryStandard.settler(),
        QueuedUnitFactoryStandard.settler(),
    ]

    build_order_expansions: List[IQueue] = [ # type: ignore
        QueuedBuildingFactory.granary(),
        QueuedBuildingFactory.library(),
        QueuedUnitFactoryStandard.chariot(),
    ]


    map = MapFromSave('resources/arabia_camel_rush.json')

    bfactory = BuildingFactory(BuildingDB('resources/Civ5CoreDatabase.db'))
    ufactory = UnitFactory(UnitDB('resources/Civ5CoreDatabase.db'))

    civ = Civ(Nation.BABYLON, bfactory, ufactory)  # found city turn 1

    capital = civ.create_city(MapHelper.get_city_tiles(map, Coord(36, 20)))
    capital.queue_up_many(build_order_capital)
    civ.queue_many_tech(build_order_tech)
    civ.queue_many_policy(build_order_policy)

    # settler_count = 0
    # settle_coords = [Coord(36, 28), Coord(28, 28), Coord(23, 23), Coord(20, 20), Coord(15, 15)]

    first_actions: List[IUnitAction] = [SettleAction(civ, 3, MapHelper.get_city_tiles(map, Coord(36, 28)))]
    civ.add_unit_made_listener(QueueUnitActions(3, first_actions))

    second_actions: List[IUnitAction] = [SettleAction(civ, 4, MapHelper.get_city_tiles(map, Coord(28, 28)))]
    civ.add_unit_made_listener(QueueUnitActions(4, second_actions))

    print("Turn 1")
    civ.stats()
    for i in range(120):
        print(f"Turn {i+2}")
        civ.next_turn()
        civ.stats()

    return civ

def new_main():
    policy_order = [
        "POLICY_LIBERTY",
        "POLICY_CITIZENSHIP",
        "POLICY_REPUBLIC",
        "POLICY_COLLECTIVE_RULE",
        "POLICY_REPRESENTATION",
        "POLICY_TRADITION"
    ]

    tech_order = [
        "TECH_ANIMAL_HUSBANDRY",
        "TECH_MINING",
        "TECH_MASONRY",
        "TECH_TRAPPING"
    ]

    capital_order = [
        "BUILDING_MONUMENT",
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

    map = MapFromSave('resources/arabia_camel_rush.json')
    civ = Civ(Nation.BABYLON, bfactory, ufactory)  # found city turn 1

    capital = civ.create_city(MapHelper.get_city_tiles(map, Coord(36, 20)))
    capital.queue_up_many(capital_order)
    civ.queue_many_tech(tech_order)
    civ.queue_many_policy(policy_order)

    print("Turn 1")
    civ.stats()
    for i in range(120):
        print(f"Turn {i+2}")
        civ.next_turn()
        civ.stats()



if __name__ == "__main__":
    # main()
    # test_arabia_camel_archer_rush()
    new_main()
