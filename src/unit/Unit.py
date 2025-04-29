# pyright: strict

from typing import List
from core.Coord import Coord
from unit.IUnitAction import IUnitAction
from unit.IUnit import IUnit

class Unit(IUnit):
    num_units = 0
    
    def __init__(self, name: str, coord: Coord):
        self._id = Unit.num_units
        Unit.num_units += 1

        self.name = name
        self._coord = coord
        self.action_queue: List[IUnitAction] = []

    @property
    def coord(self) -> Coord:
        return self._coord
    
    
    @coord.setter
    def coord(self, value: Coord):
        self._coord = value

    @property
    def id(self) -> int:
        return self._id
    
    def next_turn(self):
        if not self.action_queue:
            return

        curr_action = self.action_queue[0]

        if not curr_action.destination:
            self.action_queue.pop(0)
            return

        if self.coord != curr_action.destination:
            self.move_towards_destination(curr_action.destination)
        else:
            curr_action.execute()
            self.action_queue.pop(0)

    def move_towards_destination(self, destination: Coord):
        """Moves 1 step closer to destination"""

        if self.coord.x < destination.x:
            self.coord += Coord(1, 0)
        elif self.coord.x > destination.x:
            self.coord -= Coord(1, 0)

        if self.coord.y < destination.y:
            self.coord += Coord(0, 1)
        elif self.coord.y > destination.y:
            self.coord -= Coord(0, 1)

    def insert(self, index: int, action: IUnitAction):
        self.action_queue.insert(index, action)

    def queue(self, action: IUnitAction):
        self.action_queue.append(action)

    def __repr__(self):
        return f"{self.name} @ {self.coord}"
