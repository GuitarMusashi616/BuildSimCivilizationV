# pyright: basic

from typing import List
import unittest

from adapter.QueueUnitActions import QueueUnitActions
from commands.NewCiv import NewCiv
from commands.SettleUnit import SettleUnit
from commands.TrainUnit import TrainUnit
# from core.Game import Game
from core.Civ import Civ
from core.Coord import Coord
from core.ICiv import ICiv
from enums.Nation import Nation
from map.MapFactory import MapFactory
from queueable.QueuedUnitFactory import QueuedUnitFactory
from unit.IUnit import IUnit
from unit.IUnitAction import IUnitAction
from unit.SettleAction import SettleAction
from unit.Unit import Unit
from unit.UnitType import UnitType

class TestUnits(unittest.TestCase):
    # def test_settlers(self):
    #     game = Game()

    #     game.handle(NewCiv(1337, Nation.ARABIA, 11))

    #     game.handle(SettleUnit(1337, 11, 100))

    #     game.handle(TrainUnit(1337, 100, UnitType.WORKER))

    #     civ = game.civ_repo.get(1337)
    #     civ.stats()



    def test_workers(self):
        # civ = Civ(Nation.ARABIA)

        worker = QueuedUnitFactory.worker()

        worker.next_turn()
    
    def test_unit_made_listener(self):
        base = MapFactory.arabiabase(Coord(35, 20))
        civ: ICiv = Civ(Nation.ARABIA)
        actions: List[IUnitAction] = [SettleAction(civ, 0, base)]

        listener = QueueUnitActions(0, actions)

        civ.add_unit_made_listener(listener)

        civ.add_unit(Unit(UnitType.SETTLER, base[0].coord))
        civ.stats()
        assert isinstance(civ.units[0], Unit) and len(civ.units[0].action_queue) > 0




if __name__ == "__main__":
    unittest.main()