# pyright: strict

from core.Coord import Coord
from unit.IUnitAction import IUnitAction


class RestAction(IUnitAction):
    """Does nothing for a turn"""

    def __init__(self, destination: Coord):
        self._destination = destination

    def execute(self):
        pass
    
    @property
    def destination(self) -> Coord | None:
        return None