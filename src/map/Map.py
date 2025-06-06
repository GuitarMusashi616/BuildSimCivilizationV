# pyright: strict

# http://devmag.org.za/2013/08/31/geometry-with-hex-coordinates/

from __future__ import annotations
from typing import Dict, List, Tuple
from core.Coord import Coord
from map.IMap import IMap
from map.MapHelper import MapHelper
from tile.ITile import ITile
from tile.TerrainType import TerrainType
from tile.Tile import Tile


class Map(IMap):
    """A formula to take a bunch of hexes and attach coordinates to it"""

    def __init__(self, coord_to_tile: Dict[Tuple[int, int], ITile]):
        self.coord_to_tile = coord_to_tile
    
    def get_tile(self, coord: Coord) -> ITile:
        return self.coord_to_tile[coord.x, coord.y]

    def __repr__(self) -> str:
        return f"{self.coord_to_tile}"
    
    def get_city_tiles(self, center: Coord) -> List[ITile]:
        """Returns the clockwise order of tiles from the map starting from the middle"""
        return MapHelper.get_city_tiles(self, center)

    def get_width_height(self) -> Tuple[int, int]:
        return (20, 20)
    
    @staticmethod
    def coord_gen(col_low: int, col_high: int, row_high: int, row_low: int) -> List[Coord]:
        output: List[Coord] = []
        for row in range(row_high, row_low, -1):
            for col in range(col_low, col_high):
                output.append(Coord(col, row))

            if row%2==1:
                col_high += 1
            else:
                col_low += 1

        return output
    
    @staticmethod
    def grassmap(col_low: int = -5, col_high: int = 3, row_high: int = 3, row_low: int = -4) -> Map:
        ls = Map.coord_gen(col_low, col_high, row_high, row_low)
        coord_to_tile: Dict[Tuple[int, int], ITile] = {}

        for coord in ls:
            coord_to_tile[coord.x, coord.y] = Tile(coord, TerrainType.GRASSLAND)

        return Map(coord_to_tile)



if __name__ == "__main__":
    # ls = Map.coord_gen(-5, 3, 3, -4)
    ls = Map.grassmap()
    print(ls)