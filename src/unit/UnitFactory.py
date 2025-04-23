# pyright: strict



from core.Coord import Coord
from queueable.IQueue import IQueue
from queueable.QueuedUnit import QueuedUnit
from queueable.StaticQueuedUnit import StaticQueuedUnit
from unit.IUnit import IUnit
from unit.IUnitDB import IUnitDB
from unit.IUnitFactory import IUnitFactory
from unit.Unit import Unit
from unit.UnitOld import UnitOld
from unit.UnitType import UnitType


class UnitFactory(IUnitFactory):
    def __init__(self, unit_db: IUnitDB):
        self.unit_db = unit_db

    def create_queueable(self, unit: str) -> IQueue:
        cost = self.unit_db.get_cost(unit)
        return QueuedUnit(unit, cost)

    def create(self, unit: str, coord: Coord) -> IUnit:
        return Unit(unit, coord)

    @staticmethod
    def instantiate(queueable: IQueue, coord: Coord) -> IUnit:
        if isinstance(queueable, StaticQueuedUnit):
            return UnitOld(UnitType[queueable.name], coord)

        return Unit(queueable.name, coord)