# pyright: strict

from typing import List
from core.City import City
from core.Civ import Civ
from enums.Nation import Nation
from researchable.Policy import Policy
from researchable.Tech import Tech
from queueable.UnitFactory import UnitFactory
from queueable.WonderFactory import WonderFactory
from tile.ITile import ITile
from tile.TileFactory import TileFactory

def main():
    # first tile is the city
    # then start above it going clockwise (start on upper right if two tiles above first tile)
    civ = Civ(Nation.ARABIA)

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

    capital = City(base)
    capital.add_wonder(WonderFactory.palace())
    capital.pick_tiles_with_strat()
    capital.queue_up(UnitFactory.worker())

    civ.add_city(capital, 1)

    civ.queue_research(Tech('Pottery', 25))
    civ.queue_policy(Policy('Oligarchy'))
    civ.stats()

    for i in range(2, 100):
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