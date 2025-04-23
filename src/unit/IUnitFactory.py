# pyright: strict

from abc import ABC, abstractmethod

from core.Coord import Coord
from queueable.IQueue import IQueue
from unit.IUnit import IUnit

class IUnitFactory(ABC):

    @abstractmethod
    def create_queueable(self, unit: str) -> IQueue:
        """Creates an IQueueable from a string eg. BUILDING_MONUMENT"""

    @abstractmethod
    def create(self, unit: str, coord: Coord) -> IUnit:
        """Creates an IBuilding from a string eg. BUILDING_MONUMENT"""
