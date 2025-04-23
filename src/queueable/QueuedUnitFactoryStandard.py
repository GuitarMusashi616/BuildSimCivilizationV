from queueable.QueuedUnit import QueuedUnit
from unit.UnitType import UnitType


class QueuedUnitFactoryStandard:
    @staticmethod
    def settler() -> QueuedUnit:
        return QueuedUnit(UnitType.SETTLER, 106)
    
    @staticmethod
    def worker() -> QueuedUnit:
        return QueuedUnit(UnitType.WORKER, 70)

    @staticmethod
    def warrior() -> QueuedUnit:
        return QueuedUnit(UnitType.WARRIOR, 40)

    @staticmethod
    def scout() -> QueuedUnit:
        return QueuedUnit(UnitType.SCOUT, 25)

    @staticmethod
    def chariot() -> QueuedUnit:
        return QueuedUnit(UnitType.CHARIOT_ARCHER, 56)