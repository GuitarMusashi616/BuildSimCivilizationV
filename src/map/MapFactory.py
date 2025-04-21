# pyright: strict

from typing import Dict, List, Tuple
from core.Coord import Coord
from map.IMap import IMap
from map.Map import Map
from map.MapFromSave import MapFromSave
from map.MapHelper import MapHelper
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
    
    @staticmethod
    def arabiamap() -> IMap:
        mapsave: IMap = MapFromSave('resources/arabia_camel_rush.json')
        return mapsave
    
    @staticmethod
    def arabiabase(center: Coord) -> List[ITile]:
        return MapHelper.get_city_tiles(MapFactory.arabiamap(), center)