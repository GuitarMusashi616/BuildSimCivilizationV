# pyright: basic

from typing import List
from src.Resource import Resource
from src.Tile import Tile


class TileFactory:
    @staticmethod
    def grassland(resources: List[Resource] | None = []) -> Tile:
        return Tile(2, 0, 0, resources if resources else [], [])
    
    @staticmethod
    def grassland_hill(resources: List[Resource] | None = []) -> Tile:
        return Tile(0, 2, 0, resources if resources else [], [])
    
    @staticmethod
    def grassland_river(resources: List[Resource] | None = []) -> Tile:
        return Tile(0, 2, 0, resources if resources else [], [])
    
    @staticmethod
    def forest_grassland(resources: List[Resource] | None = []) -> Tile:
        return Tile(1, 1, 0, resources if resources else [], [])
    
    @staticmethod
    def plains_river(resources: List[Resource] | None = []) -> Tile:
        return Tile(1, 1, 0, resources if resources else [], [])