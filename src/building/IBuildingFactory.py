# pyright: strict

from abc import ABC, abstractmethod

from building.IBuilding import IBuilding
from queueable.IQueue import IQueue

class IBuildingFactory(ABC):

    @abstractmethod
    def instantiate(self, queueable: IQueue) -> IBuilding:
        """Returns a fully instantiated building"""

    @abstractmethod
    def create_queueable(self, building: str) -> IQueue:
        """Creates an IQueueable from a string eg. BUILDING_MONUMENT"""

    @abstractmethod
    def create(self, building: str) -> IBuilding:
        """Creates an IBuilding from a string eg. BUILDING_MONUMENT"""
