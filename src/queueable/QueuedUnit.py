# pyright: strict

from core.Coord import Coord
from core.ICity import ICity
from queueable.IQueue import IQueue
from unit.IUnit import IUnit
from unit.Unit import Unit
from unit.UnitType import UnitType

class QueuedUnit(IQueue):
    def __init__(self, unit_type: UnitType, hammers_req: int):
        self.unit_type = unit_type
        self._hammers_req = hammers_req

    def next_turn(self):
        # affected by land
        pass

    @property
    def name(self) -> str: # type: ignore
        return self.unit_type.name

    @property
    def hammers_req(self) -> int:
        return self._hammers_req
    
    def convert(self, city: ICity) -> IUnit:
        return self.to_unit(city.tiles[0].coord)

    def to_unit(self, coord: Coord) -> Unit:
        return Unit(self.unit_type, coord)
    
    def __repr__(self):
        return f"{self.name}({self.hammers_req})"


    