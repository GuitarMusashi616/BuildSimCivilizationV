# pyright: strict

from building.Building import Building
from building.IBuilding import IBuilding
from building.IBuildingDB import IBuildingDB
from building.IBuildingFactory import IBuildingFactory
from core.ICity import ICity
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

    def instantiate(self, queueable: IQueue, city: ICity) -> IBuilding:
        """Returns a fully instantiated unit or building"""
        if (isinstance(queueable, StaticQueuedBuilding)):
            return queueable
        
        self.apply_resource_yield_changes(queueable.name, city)
        
        return self.create(queueable.name)
    
    def apply_resource_yield_changes(self, building: str, city: ICity):
        """Changes the tiles around the base because of newly constructed building ie +1 food for wheat from granary"""
        changes = self.building_db.get_resource_yield_changes(building)
        for tile in city.tiles:
            if tile.resource.name not in changes:
                continue
            tile.add_yield_change(changes[tile.resource.name])
        