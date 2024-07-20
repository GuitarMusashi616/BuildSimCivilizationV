# pyright: basic

from typing import List
from City import City
from Resource import Resource
from Improvement import Improvement
from Tile import Tile
from WonderFactory import WonderFactory
from src.TileFactory import TileFactory

def main():
    # first tile is the city
    # then start above it going clockwise (start on upper right if two tiles above first tile)
    base = [
        TileFactory.grassland_river(),
        TileFactory.grassland_hill(),
        TileFactory.forest_grassland(),
        TileFactory.grassland_river(),
        TileFactory.grassland_river(),
        TileFactory.plains_river(),
        TileFactory.grassland_river([Resource.STONE]),
    ]

    capital = City()

    capital.add_wonder(WonderFactory.palace())

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



main()