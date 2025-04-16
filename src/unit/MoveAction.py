from core.Coord import Coord
from unit.IUnitAction import IUnitAction


class MoveAction(IUnitAction):
    def __init__(self, destination: Coord):
        self._destination = destination

    def execute(self):
        pass
    
    @property
    def destination(self) -> Coord:
        return self._destination