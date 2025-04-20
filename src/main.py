# pyright: strict

from typing import List
from core.Civ import Civ
from core.Coord import Coord
from enums.Nation import Nation
from queueable.BuildingFactory import BuildingFactory
from queueable.IQueue import IQueue
from queueable.UnitFactoryStandard import UnitFactoryStandard
from researchable.Tech import Tech
from researchable.Policy import Policy
from queueable.UnitFactory import UnitFactory
from tile.ITile import ITile
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.Tile import Tile

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
    civ = Civ(Nation.ARABIA)

    capital = civ.create_city(get_base())
    capital.queue_up(UnitFactory.worker())

    civ.queue_research(Tech('Pottery', 25))
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
        UnitFactoryStandard.scout(),
        UnitFactoryStandard.scout(),
        BuildingFactory.granary(),
        UnitFactoryStandard.scout(),
        UnitFactoryStandard.settler(),
        UnitFactoryStandard.settler(),
    ]

    build_order_expansions: List[IQueue] = [ # type: ignore
        BuildingFactory.granary(),
        BuildingFactory.library(),
        UnitFactoryStandard.chariot(),
    ]


    civ = Civ(Nation.BABYLON)  # found city turn 1

    capital = civ.create_city(get_base())
    capital.queue_up_many(build_order_capital)

    civ.queue_many_research(build_order_tech)
    civ.queue_many_policy(build_order_policy)
    return civ



def main2():
    pass
    # expected output, food, prod, science, gold, culture, faith

    # end turn 1

    # science = 0/25 (+4) [7 turns]
    # researched = [agriculture]

    # gold = 22 (+3)
    # happiness = 5 (+9, -4)

    # culture = 0/15 (+1) [15 turns]
    # researched = [garrison(tradition)]

    # faith = 0/6 (+0) [inf turns]

    # city 1
        # pop: 1, growth: 20/30 (+2) [5 turns]
        # prod: 'worker' 0/46 (+5) [10 turns]

        # gold: +3
        # science: +4
        # faith: +0
        # tourism: +0
        # culture: +1, border growth (0/10)

        # tiles: []
        # buildings: []
        # wonders: []


    # units = {warrior: 1, scout: 2}


if __name__ == "__main__":
    main()