# pyright: strict

from core.Coord import Coord
from unit.UnitActionType import UnitActionType


class UnitAction:
    def __init__(self, action_type: UnitActionType, destination: Coord):
        self.action_type = action_type
        self.destination = destination
    
    def execute(self):
        pass