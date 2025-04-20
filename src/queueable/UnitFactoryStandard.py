from queueable.UnitInProgress import UnitInProgress
from unit.UnitType import UnitType


class UnitFactoryStandard:
    @staticmethod
    def settler() -> UnitInProgress:
        return UnitInProgress(UnitType.SETTLER, 106)
    
    @staticmethod
    def worker() -> UnitInProgress:
        return UnitInProgress(UnitType.WORKER, 70)

    @staticmethod
    def warrior() -> UnitInProgress:
        return UnitInProgress(UnitType.WARRIOR, 40)

    @staticmethod
    def scout() -> UnitInProgress:
        return UnitInProgress(UnitType.SCOUT, 25)

    @staticmethod
    def chariot() -> UnitInProgress:
        return UnitInProgress(UnitType.CHARIOT_ARCHER, 56)