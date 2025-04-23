# pyright: strict

from typing import List
from building.IBuildingFactory import IBuildingFactory
from queueable.IQueue import IQueue
from unit.IUnitFactory import IUnitFactory

class QueueFactory:
    def __init__(self, building_factory: IBuildingFactory, unit_factory: IUnitFactory):
        self.building_factory = building_factory
        self.unit_factory = unit_factory

    def from_string(self, building_or_unit: str) -> IQueue:
        if 'BUILDING' in building_or_unit:
            return self.building_factory.create_queueable(building_or_unit)
        return self.unit_factory.create_queueable(building_or_unit)
    
    def from_string_list(self, buildings_and_units: List[str]) -> List[IQueue]:
        return [self.from_string(x) for x in buildings_and_units]
        