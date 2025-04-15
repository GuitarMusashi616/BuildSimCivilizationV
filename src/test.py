# pyright: strict

from typing import List
from queueable.BuildingFactory import BuildingFactory
from core.City import City
from core.Civ import Civ
from enums.Nation import Nation
from queueable.IQueue import IQueue
from researchable.PolicyFactory import PolicyFactory
from researchable.TechFactory import TechFactory
from tile.ITile import ITile
from tile.TileFactory import TileFactory
from queueable.UnitFactory import UnitFactory
from queueable.WonderFactory import WonderFactory

def babylon_race_fixture() -> Civ:
    build_order_capital: List[IQueue] = [UnitFactory.worker(), BuildingFactory.granary(), WonderFactory.great_library()]
    build_order_tech = [TechFactory.pottery(), TechFactory.writing()]
    build_order_policy = [PolicyFactory.oligarchy()]

    base: List[ITile] = [
        TileFactory.grassland_river_city(),
        TileFactory.grassland_hill(),
        TileFactory.forest_grassland(),
        TileFactory.grassland_river(),
        TileFactory.grassland_river(),
        TileFactory.plains_river(),
        TileFactory.grassland_river_stone(),

        TileFactory.grassland_hill(),
        TileFactory.forest_grassland(),
        TileFactory.grassland_river(),
        TileFactory.grassland_river(),
        TileFactory.plains_river(),
        TileFactory.grassland_river_stone(),
    ]

    civ = Civ(Nation.BABYLON)  # found city turn 1

    capital = City(base)
    capital.add_wonder(WonderFactory.palace())
    capital.pick_tiles_with_strat()
    capital.queue_up_many(build_order_capital)

    civ.add_city(capital, 1)

    civ.queue_many_research(build_order_tech)
    civ.queue_many_policy(build_order_policy)
    return civ


def test():
    base: List[ITile] = [
        TileFactory.grassland_river_city(),
        TileFactory.grassland_hill(),
        TileFactory.forest_grassland(),
        TileFactory.grassland_river(),
        TileFactory.grassland_river(),
        TileFactory.plains_river(),
        TileFactory.grassland_river_stone(),
    ]


    civ1 = Civ(Nation.BABYLON)
    civ2 = Civ(Nation.ARABIA)
    city1 = City(base)
    city1.pop = 5
    city2 = City(base)
    city2.pop = 7

    civ1.add_city(city1, 1)
    civ1.add_city(city2, 2)
    civ2.add_city(City(base), 1)

    print([x.pop for x in civ1.cities.values()])
    print([x.pop for x in civ2.cities.values()])


    a = TileFactory.grassland()
    b = TileFactory.grassland()

    print(a.__dict__)
    print(b.__dict__)


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