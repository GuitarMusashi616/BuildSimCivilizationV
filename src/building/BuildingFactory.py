# pyright: strict

from building.IBuilding import IBuilding
from queueable.IQueue import IQueue
from queueable.QueuedBuilding import QueuedBuilding


class BuildingFactory:
    @staticmethod
    def instantiate(queueable: IQueue) -> IBuilding:
        """Returns a fully instantiated unit or building"""

        assert isinstance(queueable, QueuedBuilding), "Must be queueable building"
        return queueable

        