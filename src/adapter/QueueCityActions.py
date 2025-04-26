# pyright: strict

from __future__ import annotations
from typing import List
from adapter.ICityMadeListener import ICityMadeListener
from core.ICity import ICity
from queueable.IQueue import IQueue


class QueueCityActions(ICityMadeListener):
    def __init__(self, cityId: int, action_queue: List[IQueue]):
        self.cityId = cityId
        self.action_queue = action_queue

    def notify(self, city: ICity):
        if city.id != self.cityId:
            return
        
        city.queue_up_many(self.action_queue)
        
