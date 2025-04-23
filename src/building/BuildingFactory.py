# pyright: strict

from building.Building import Building
from building.IBuilding import IBuilding
from building.IBuildingDB import IBuildingDB
from building.IBuildingFactory import IBuildingFactory
from queueable.IQueue import IQueue
from queueable.QueuedBuilding import QueuedBuilding
from queueable.StaticQueuedBuilding import StaticQueuedBuilding


class BuildingFactory(IBuildingFactory):
    def __init__(self, building_db: IBuildingDB):
        self.building_db = building_db

    def create_queueable(self, building: str) -> IQueue:
        cost = self.building_db.get_cost(building)
        return QueuedBuilding(building, cost)

    def create(self, building: str) -> IBuilding:
        output = self.building_db.get_yields(building)
        return Building(building, output)

    def instantiate(self, queueable: IQueue) -> IBuilding:
        """Returns a fully instantiated unit or building"""
        if (isinstance(queueable, StaticQueuedBuilding)):
            return queueable

        return self.create(queueable.name)


        