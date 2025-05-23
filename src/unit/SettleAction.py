# pyright: strict

from typing import List
from core.Coord import Coord
from core.ICiv import ICiv
from tile.ITile import ITile
from unit.IUnitAction import IUnitAction


class SettleAction(IUnitAction):
    def __init__(self, civ: ICiv, unitId: int, base: List[ITile]):
        self.civ = civ
        self.unitId = unitId
        self.base = base
        self._destination = base[0].coord
    
    @property
    def destination(self) -> Coord:
        return self._destination

    def execute(self):
        self.civ.create_city(self.base)
        self.civ.remove_unit(self.unitId)
        # self.civ.map.get_tiles?