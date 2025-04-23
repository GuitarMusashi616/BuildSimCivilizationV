from queueable.StaticQueuedUnit import StaticQueuedUnit
from unit.UnitType import UnitType


class QueuedUnitFactoryStandard:
    @staticmethod
    def settler() -> StaticQueuedUnit:
        return StaticQueuedUnit(UnitType.SETTLER, 106)
    
    @staticmethod
    def worker() -> StaticQueuedUnit:
        return StaticQueuedUnit(UnitType.WORKER, 70)

    @staticmethod
    def warrior() -> StaticQueuedUnit:
        return StaticQueuedUnit(UnitType.WARRIOR, 40)

    @staticmethod
    def scout() -> StaticQueuedUnit:
        return StaticQueuedUnit(UnitType.SCOUT, 25)

    @staticmethod
    def chariot() -> StaticQueuedUnit:
        return StaticQueuedUnit(UnitType.CHARIOT_ARCHER, 56)