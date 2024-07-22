# pyright: basic

from typing import List
from enums.Resource import Resource
from tile.Tile import Tile


class TileFactory:
    @staticmethod
    def grassland() -> Tile:
        return Tile(
            food = 2,
            prod = 0,
            gold = 0,
            culture = 0,
            science = 0,
            faith = 0,
        )
    
    @staticmethod
    def grassland_hill() -> Tile:
        return Tile(
            food = 0,
            prod = 2,
            gold = 0,
            culture = 0,
            science = 0,
            faith = 0,
        )
    
    @staticmethod
    def grassland_river() -> Tile:
        return Tile(
            food = 2,
            prod = 0,
            gold = 0,
            culture = 0,
            science = 0,
            faith = 0,
        )

    @staticmethod
    def grassland_river_city() -> Tile:
        return Tile(
            food = 2,
            prod = 1,
            gold = 0,
            culture = 0,
            science = 0,
            faith = 0,
        )

    @staticmethod
    def grassland_river_stone() -> Tile:
        return Tile(
            food = 2,
            prod = 1,
            gold = 0,
            culture = 0,
            science = 0,
            faith = 0,
        )
    
    @staticmethod
    def forest_grassland() -> Tile:
        return Tile(
            food = 1,
            prod = 1,
            gold = 0,
            culture = 0,
            science = 0,
            faith = 0,
        )
    
    @staticmethod
    def plains_river() -> Tile:
        return Tile(
            food = 1,
            prod = 1,
            gold = 0,
            culture = 0,
            science = 0,
            faith = 0,
        )