from core.Civ import Civ
from core.Coord import Coord
from unit.IUnitAction import IUnitAction


class SettleAction(IUnitAction):
    def __init__(self, civ: Civ, destination: Coord):
        self.civ = civ
        self._destination = destination
    
    @property
    def destination(self) -> Coord:
        return self._destination

    def execute(self):
        self.civ.create_city()
        # self.civ.map.get_tiles?