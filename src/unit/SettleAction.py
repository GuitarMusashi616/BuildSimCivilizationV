# pyright: strict

from typing import List
from core.Civ import Civ
from core.Coord import Coord
from tile.ITile import ITile
from unit.IUnitAction import IUnitAction
from unit.Unit import Unit


class SettleAction(IUnitAction):
    def __init__(self, civ: Civ, unit: Unit, base: List[ITile]):
        self.civ = civ
        self.unit = unit
        self.base = base
        self._destination = base[0].coord
    
    @property
    def destination(self) -> Coord:
        return self._destination

    def execute(self):
        self.civ.create_city(self.base)
        self.civ.remove_unit(self.unit.id)
        # self.civ.map.get_tiles?