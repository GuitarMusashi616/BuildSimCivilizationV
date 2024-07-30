# pyright: strict

import unittest

from commands.NewCiv import NewCiv
from commands.SettleUnit import SettleUnit
from commands.TrainUnit import TrainUnit
from core.Game import Game
from enums.Nation import Nation
from queueable.UnitFactory import UnitFactory
from queueable.UnitType import UnitType

class TestUnits(unittest.TestCase):
    def test_settlers(self):
        game = Game()

        game.handle(NewCiv(1337, Nation.ARABIA, 11))

        game.handle(SettleUnit(1337, 11, 100))

        game.handle(TrainUnit(1337, 100, UnitType.WORKER))

        civ = game.civ_repo.get(1337)
        civ.stats()



    def test_workers(self):
        # civ = Civ(Nation.ARABIA)

        worker = UnitFactory.worker()

        worker.next_turn()



if __name__ == "__main__":
    unittest.main()