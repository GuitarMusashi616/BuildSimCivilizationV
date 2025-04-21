# pyright: strict

from typing import List
from core.Coord import Coord
from map.IMap import IMap
from tile.ITile import ITile


class MapHelper:
    city_tiles_offset = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, 1),

        (-1, 2),
        (0, 2),
        (1, 1),
        (2, 0),
        (2, -1),
        (2, -2),
        (1, -2),
        (0, -2),
        (-1, -1),
        (-2, 0),
        (-2, 1),
        (-2, 2),

        (-1, 3),
        (0, 3),
        (1, 2),
        (2, 1),
        (3, 0),
        (3, -1),
        (3, -2),
        (3, -3),
        (2, -3),
        (1, -3),
        (0, -3),
        (-1, -2),
        (-2, -1),
        (-3, 0),
        (-3, 1),
        (-3, 2),
        (-3, 3),
        (-2, 3),
    ]

    @staticmethod
    def get_city_tiles(map: IMap, center: Coord) -> List[ITile]:
        """Returns the clockwise order of tiles from the map starting from the middle"""
        output: List[ITile] = []
        for xoff,yoff in MapHelper.city_tiles_offset:
            coord = center + Coord(xoff, yoff)
            output.append(map.get_tile(coord))
        return output
