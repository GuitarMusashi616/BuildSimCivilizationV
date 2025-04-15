# pyright: strict

from core.Coord import Coord
from unit.UnitType import UnitType
from unit.IUnit import IUnit

class Unit(IUnit):
    def __init__(self, unit_type: UnitType, coord: Coord):
        self.unit_type = unit_type
        self._coord = coord

    @property
    def coord(self) -> Coord:
        return self._coord
    
    def next_turn(self):
        pass