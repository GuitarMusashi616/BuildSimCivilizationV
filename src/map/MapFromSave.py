# pyright: strict

import json

from core.Coord import Coord
from map.IMap import IMap
from tile.ITile import ITile
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.Tile import Tile
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

    def get_tile(self, coord: Coord) -> ITile:
        try: 
            maptile = self.tiles[coord.y][coord.x]
            terrain = self.terrain[maptile['TerrainType']]
            resource = self.resource[maptile['ResourceType']] if maptile['ResourceType'] != 255 else "NONE"
            # feature = self.resource[maptile['FeatureTerrainType']] if maptile['FeatureTerrainType'] != 255 else "NONE"

            return Tile(coord, TerrainType[terrain], ResourceType[resource])

            # return TileString(coord, terrain, resource, feature)
        except IndexError:
            raise IndexError(f"Can't find {coord} in map from save file {self.filename}")
    
    def __del__(self):
        self.file.close()
    



    
