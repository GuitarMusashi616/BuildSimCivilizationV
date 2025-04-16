# pyright: strict

from typing import Dict, Tuple
from map.IMap import IMap
from map.Map import Map
from tile.ITile import ITile
from tile.TerrainType import TerrainType
from tile.Tile import Tile


class MapFactory:
    @staticmethod
    def grassmap() -> IMap:
        ls = Map.coord_gen(-5, 3, 3, -4)
        coord_to_tile: Dict[Tuple[int, int], ITile] = {}

        for coord in ls:
            coord_to_tile[coord.x, coord.y] = Tile(coord, TerrainType.GRASSLAND)

        return Map(coord_to_tile)