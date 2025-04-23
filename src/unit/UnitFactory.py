# pyright: strict



from core.Coord import Coord
from queueable.IQueue import IQueue
from unit.IUnit import IUnit
from unit.Unit import Unit
from unit.UnitType import UnitType


class UnitFactory:
    @staticmethod
    def instantiate(queueable: IQueue, coord: Coord) -> IUnit:
        return Unit(UnitType[queueable.name], coord)