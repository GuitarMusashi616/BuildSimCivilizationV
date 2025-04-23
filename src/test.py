# pyright: strict

from typing import List
from building.BuildingDB import BuildingDB
from building.BuildingFactory import BuildingFactory
from core.Coord import Coord
from queueable.QueuedBuildingFactory import QueuedBuildingFactory
from core.Civ import Civ
from enums.Nation import Nation
from queueable.IQueue import IQueue
from researchable.PolicyFactory import PolicyFactory
from researchable.TechFactory import TechFactory
from tile.ITile import ITile
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.Tile import Tile
from queueable.QueuedUnitFactory import QueuedUnitFactory
from queueable.QueuedWonderFactory import QueuedWonderFactory
from unit.UnitDB import UnitDB
from unit.UnitFactory import UnitFactory

def babylon_race_fixture() -> Civ:
    build_order_capital: List[IQueue] = [QueuedUnitFactory.worker(), QueuedBuildingFactory.granary(), QueuedWonderFactory.great_library()]
    build_order_tech = [TechFactory.pottery(), TechFactory.writing()]
    build_order_policy = [PolicyFactory.oligarchy()]

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

    bfactory = BuildingFactory(BuildingDB('resources/Civ5CoreDatabase.db'))
    ufactory = UnitFactory(UnitDB('resources/Civ5CoreDatabase.db'))
    civ = Civ(Nation.BABYLON, bfactory, ufactory)  # found city turn 1

    capital = civ.create_city(base)
    capital.queue_up_many(build_order_capital)

    civ.queue_many_tech(build_order_tech)
    civ.queue_many_policy(build_order_policy)
    return civ


# def test():
#     base: List[ITile] = [
#         Tile(Coord(1, 1), TerrainType.GRASSLAND_RIVER),
#         Tile(Coord(1, 0), TerrainType.GRASSLAND_HILL),
#         Tile(Coord(2, 0), TerrainType.FOREST_GRASSLAND),
#         Tile(Coord(2, 1), TerrainType.GRASSLAND_RIVER),
#         Tile(Coord(1, 2), TerrainType.GRASSLAND_RIVER),
#         Tile(Coord(0, 1), TerrainType.PLAINS_RIVER),
#         Tile(Coord(0, 0), TerrainType.GRASSLAND_RIVER, ResourceType.STONE),
#     ]

#     civ1 = Civ(Nation.BABYLON)
#     civ2 = Civ(Nation.ARABIA)
#     city1 = civ1.create_city([])
#     city1.pop = 5
#     city2 = civ2.create_city([])
#     city2.pop = 7
#     civ2.create_city(base)


#     print([x.pop for x in civ1.cities.values()])
#     print([x.pop for x in civ2.cities.values()])


#     a = Tile(Coord(0, 0), TerrainType.GRASSLAND_HILL),
#     b = Tile(Coord(1, 0), TerrainType.GRASSLAND_HILL),

#     print(a.__dict__)
#     print(b.__dict__)


def babylon_race():
    """Rush building the great library as babylon, show what happens every turn"""

    civ = babylon_race_fixture()

    for i in range(1, 100):
        print(f"TURN {i}")
        print()
        civ.stats()
        civ.next_turn()


def unit_city_actions():
    """Be able to queue actions like Settle() for units and rearrange priority?"""
    civ = babylon_race_fixture()

    for i in range(1, 100):
        print(f"TURN {i}")
        print()
        civ.stats()
        civ.next_turn()


if __name__ == "__main__":
    unit_city_actions()