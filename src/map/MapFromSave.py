# pyright: strict

import json
from typing import Tuple

from core.Coord import Coord
from map.IMap import IMap
from tile.FeatureType import FeatureType
from tile.ITile import ITile
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.TileFeature import TileFeature
# from tile.TileString import TileString

class MapFromSave(IMap):
    """Gets the map from the json output of a .civ5map using https://github.com/samuelyuan/Civ5MapImage"""

    def __init__(self, filename: str):
        self.filename = filename
        self.file = open(filename)
        self.json = json.load(self.file)
        self.tiles = self.json['MapData']['MapTiles']
        self.resource = self.json['MapData']['ResourceList']
        self.terrain = self.json['MapData']['TerrainList']
        self.feature = self.json['MapData']['FeatureTerrainList']
    
    def get_width_height(self) -> Tuple[int, int]:
        width = self.json['MapData']['MapHeader']['Width']
        height = self.json['MapData']['MapHeader']['Height']
        return width, height

    def get_tile(self, coord: Coord) -> ITile:
        try: 
            maptile = self.tiles[coord.y][coord.x]
            terrain = self.terrain[maptile['TerrainType']]
            resource = self.resource[maptile['ResourceType']] if maptile['ResourceType'] != 255 else "NONE"
            feature = self.feature[maptile['FeatureTerrainType']] if maptile['FeatureTerrainType'] != 255 else "NONE"

            return TileFeature(coord, TerrainType[terrain], ResourceType[resource], FeatureType[feature])

            # return TileString(coord, terrain, resource, feature)
        except IndexError:
            raise IndexError(f"Can't find {coord} in map from save file {self.filename}")
    
    def __del__(self):
        self.file.close()
    



    
