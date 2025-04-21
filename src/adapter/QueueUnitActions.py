# pyright: strict

from __future__ import annotations
from typing import List
from adapter.IUnitMadeListener import IUnitMadeListener
from unit.IUnit import IUnit
from unit.IUnitAction import IUnitAction


class QueueUnitActions(IUnitMadeListener):
    def __init__(self, unitId: int, action_queue: List[IUnitAction]):
        self.unitId = unitId
        self.action_queue = action_queue

    def notify(self, unit: IUnit):
        if unit.id != self.unitId:
            return

        for action in self.action_queue:
            unit.queue(action)