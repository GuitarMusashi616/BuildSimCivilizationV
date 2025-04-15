from core.Coord import Coord
from queueable.IQueue import IQueue
from queueable.UnitInProgress import UnitInProgress
from unit.UnitType import UnitType


class UnitFactory:

    @staticmethod
    def settler() -> UnitInProgress:
        return UnitInProgress(UnitType.SETTLER, 56)
    
    @staticmethod
    def worker() -> UnitInProgress:
        return UnitInProgress(UnitType.WORKER, 46)

    @staticmethod
    def warrior() -> UnitInProgress:
        return UnitInProgress(UnitType.WARRIOR, 26)

    def spawn(self, unit_type: UnitType) -> UnitInProgress:
        if unit_type is UnitType.SETTLER:
            return self.settler()
        
        if unit_type is UnitType.WORKER:
            return self.worker()

        if unit_type is UnitType.WARRIOR:
            return self.warrior()

        assert False, "Cannot create that type of unit"