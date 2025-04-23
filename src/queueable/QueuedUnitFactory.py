from core.Coord import Coord
from queueable.IQueue import IQueue
from queueable.StaticQueuedUnit import StaticQueuedUnit
from unit.UnitType import UnitType


class QueuedUnitFactory:
    # Quick is 2/3 rounded down
    # Normal is 1x
    # Epic is 1.5x, etc


    @staticmethod
    def settler() -> StaticQueuedUnit:
        return StaticQueuedUnit(UnitType.SETTLER, 56)
        # 106 
    
    @staticmethod
    def worker() -> StaticQueuedUnit:
        return StaticQueuedUnit(UnitType.WORKER, 46)

    @staticmethod
    def warrior() -> StaticQueuedUnit:
        return StaticQueuedUnit(UnitType.WARRIOR, 26)

    @staticmethod
    def scout() -> StaticQueuedUnit:
        # 25 according to wiki
        return StaticQueuedUnit(UnitType.SCOUT, 13)
    
    def spawn(self, unit_type: UnitType) -> StaticQueuedUnit:
        if unit_type is UnitType.SETTLER:
            return self.settler()
        
        if unit_type is UnitType.WORKER:
            return self.worker()

        if unit_type is UnitType.WARRIOR:
            return self.warrior()

        assert False, "Cannot create that type of unit"