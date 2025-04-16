# pyright: strict

from core.Coord import Coord
from unit.UnitType import UnitType
from unit.IUnit import IUnit

class Unit(IUnit):
    def __init__(self, unit_type: UnitType, coord: Coord):
        self.unit_type = unit_type
        self._coord = coord
        self.destination = None

    @property
    def coord(self) -> Coord:
        return self._coord
    
    def set_destination(self, coord: Coord):
        """Moves closer to destination every turn"""
        self.destination = coord
    
    def next_turn(self):
        if self.destination is None:
            return

        if self.coord.x < self.destination.x:
            self.coord.x += 1
        elif self.coord.x > self.destination.x:
            self.coord.x -= 1

        if self.coord.y < self.destination.y:
            self.coord.y += 1
        elif self.coord.y > self.destination.y:
            self.coord.y -= 1

    def __repr__(self):
        return f"{self.unit_type.name} @ {self.coord}"
