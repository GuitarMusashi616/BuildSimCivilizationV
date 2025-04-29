# pyright: strict

from core.Coord import Coord
from core.ICiv import ICiv
from tile.ImprovementType import ImprovementType
from unit.IUnitAction import IUnitAction
from unit.RestAction import RestAction
from unit.SpawnImprovementAction import SpawnImprovementAction


class ImprovementAction(IUnitAction):
    """Go to a spot, wait a number of turns, then put an improvement there"""

    def __init__(self, civ: ICiv, city_id: int, unit_id: int, destination: Coord, turns_to_construct: int, improvement_type: ImprovementType):
        self.civ = civ
        self.city_id = city_id
        self.unit_id = unit_id
        self._destination = destination
        self.turns_to_construct = turns_to_construct
        self.improvement_type = improvement_type
    
    @property
    def destination(self) -> Coord:
        return self._destination

    def execute(self):
        unit = self.civ.get_unit(self.unit_id)
        unit.insert(1, SpawnImprovementAction(self.civ.get_city(self.city_id), self.destination, self.improvement_type))
        for _ in range(self.turns_to_construct):
            unit.insert(1, RestAction(self.destination))

        # self.civ.create_city(self.base)
        # self.civ.remove_unit(self.unitId)
        # self.civ.map.get_tiles?