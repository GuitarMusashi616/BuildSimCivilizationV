# pyright: strict

from core.Civ import Civ
from enums.Nation import Nation
from queueable.UnitFactory import UnitFactory


class CivFactory:

    @staticmethod
    def create(nation: Nation, unit_id: int = 0):
        civ = Civ(nation)
        settler = UnitFactory.settler()
        civ.add_unit(settler, unit_id)
        return civ