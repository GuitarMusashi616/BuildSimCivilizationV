from queueable.IQueue import IQueue
from queueable.Unit import Unit
from queueable.UnitType import UnitType


class UnitFactory:

    @staticmethod
    def settler() -> Unit:
        return Unit(UnitType.SETTLER, 56)
    
    @staticmethod
    def worker() -> Unit:
        return Unit(UnitType.WORKER, 46)

    @staticmethod
    def warrior() -> Unit:
        return Unit(UnitType.WARRIOR, 26)

    def spawn(self, unit_type: UnitType) -> Unit:
        if unit_type is UnitType.SETTLER:
            return self.settler()
        
        if unit_type is UnitType.WORKER:
            return self.worker()

        if unit_type is UnitType.WARRIOR:
            return self.warrior()

        assert False, "Cannot create that type of unit"