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