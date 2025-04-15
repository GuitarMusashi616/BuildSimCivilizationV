# pyright: strict

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TileOutput:
    """Keeps track of tile and improvements on that tile that make up a city"""

    food: int
    prod: int
    gold: int
    culture: int
    science: int
    faith: int

    def __add__(self, other: TileOutput):
        return TileOutput(
            food = self.food + other.food,
            prod = self.prod + other.prod,
            gold = self.gold + other.gold,
            culture = self.culture + other.culture,
            science = self.science + other.science,
            faith = self.faith + other.faith,
        )

    def __sub__(self, other: TileOutput):
        return TileOutput(
            food = self.food - other.food,
            prod = self.prod - other.prod,
            gold = self.gold - other.gold,
            culture = self.culture - other.culture,
            science = self.science - other.science,
            faith = self.faith - other.faith,
        )

    def set_minimum(self, other: TileOutput):
        """Set the minimum of each of this output factors to be at least as much as other eg. make sure this tile has at least 2 food, 1 prod, & 1 gold"""
        return TileOutput(
            food = other.food if self.food < other.food else self.food,
            prod = other.prod if self.prod < other.prod else self.prod,
            gold = other.gold if self.gold < other.gold else self.gold,
            culture = other.culture if self.culture < other.culture else self.culture,
            science = other.science if self.science < other.science else self.science,
            faith = other.faith if self.faith < other.faith else self.faith,
        )

    @staticmethod
    def minimum_if_tile_has_city() -> TileOutput:
        return TileOutput(
            food = 2,
            prod = 1,
            gold = 0,
            culture = 0,
            science = 0,
            faith = 0,
        )
    
