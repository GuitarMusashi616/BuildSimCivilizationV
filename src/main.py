# pyright: strict

from typing import List
from core.Civ import Civ
from core.Coord import Coord
from enums.Nation import Nation
from researchable.Policy import Policy
from researchable.Tech import Tech
from queueable.UnitFactory import UnitFactory
from tile.ITile import ITile
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.Tile import Tile

def main():
    # first tile is the city
    # then start above it going clockwise (start on upper right if two tiles above first tile)
    civ = Civ(Nation.ARABIA)

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

    capital = civ.create_city(base)
    capital.queue_up(UnitFactory.worker())

    civ.queue_research(Tech('Pottery', 25))
    civ.queue_policy(Policy('Oligarchy'))
    civ.stats()

    for i in range(2, 20):
        civ.next_turn()
        print(f"TURN {i}")
        print()
        civ.stats()





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