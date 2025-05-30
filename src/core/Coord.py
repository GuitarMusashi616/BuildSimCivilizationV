# pyright: strict

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Coord:
    x: int
    y: int

    def __add__(self, other: Coord):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Coord):
        return Coord(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y
        return False
    