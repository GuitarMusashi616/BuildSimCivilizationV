# pyright: strict

from core.Coord import Coord
from core.ICity import ICity
from tile.ITile import ITile
from tile.ImprovementType import ImprovementType
from unit.IUnitAction import IUnitAction


class SpawnImprovementAction(IUnitAction):
    """Instantly construct a tile improvement at destination"""

    def __init__(self, city: ICity, destination: Coord, improvement_type: ImprovementType):
        self.city = city
        self._destination = destination
        self.improvement_type = improvement_type
    
    @property
    def destination(self) -> Coord:
        return self._destination

    def execute(self):
        tile: ITile = self.city.get_tile(self.destination)
        tile.improvement = self.improvement_type

        # self.civ.create_city(self.base)
        # self.civ.remove_unit(self.unitId)