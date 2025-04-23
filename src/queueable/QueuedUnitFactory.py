from core.Coord import Coord
from queueable.IQueue import IQueue
from queueable.QueuedUnit import QueuedUnit
from unit.UnitType import UnitType


class QueuedUnitFactory:
    # Quick is 2/3 rounded down
    # Normal is 1x
    # Epic is 1.5x, etc


    @staticmethod
    def settler() -> QueuedUnit:
        return QueuedUnit(UnitType.SETTLER, 56)
        # 106 
    
    @staticmethod
    def worker() -> QueuedUnit:
        return QueuedUnit(UnitType.WORKER, 46)

    @staticmethod
    def warrior() -> QueuedUnit:
        return QueuedUnit(UnitType.WARRIOR, 26)

    @staticmethod
    def scout() -> QueuedUnit:
        # 25 according to wiki
        return QueuedUnit(UnitType.SCOUT, 13)
    
    def spawn(self, unit_type: UnitType) -> QueuedUnit:
        if unit_type is UnitType.SETTLER:
            return self.settler()
        
        if unit_type is UnitType.WORKER:
            return self.worker()

        if unit_type is UnitType.WARRIOR:
            return self.warrior()

        assert False, "Cannot create that type of unit"