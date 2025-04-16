# # pyright: strict

# from typing import Any
# from commands.DeleteUnitHandler import DeleteUnitHandler
# from commands.NewCiv import NewCiv
# from commands.NewCivHandler import NewCivHandler
# from commands.SettleUnit import SettleUnit
# from commands.SettleUnitHandler import SettleUnitHandler
# from commands.SpawnCityHandler import SpawnCityHandler
# from commands.TrainUnit import TrainUnit
# from commands.TrainUnitHandler import TrainUnitHandler
# from core.CityFactory import CityFactory
# from core.CivFactory import CivFactory
# from queueable.UnitFactory import UnitFactory
# from repositories.CivRepo import CivRepo
# from functools import singledispatchmethod


# class Game:
#     def __init__(self):
#         self.civ_repo: CivRepo = CivRepo()

#         self.civ_factory: CivFactory = CivFactory()
#         self.city_factory: CityFactory = CityFactory()
#         self.unit_factory: UnitFactory = UnitFactory()

#         self.new_civ_handler: NewCivHandler = NewCivHandler(self.civ_factory, self.civ_repo)
#         self.settle_unit_handler: SettleUnitHandler = SettleUnitHandler(DeleteUnitHandler(self.civ_repo), SpawnCityHandler(self.civ_repo, self.city_factory))
#         self.train_unit_handler: TrainUnitHandler = TrainUnitHandler(self.civ_repo, self.unit_factory)

#     @singledispatchmethod
#     def handle(self, command: Any) -> None:
#         raise NotImplementedError("Unsupported type")

#     @handle.register
#     def _(self, command: NewCiv) -> None:
#         self.new_civ_handler.handle(command)

#     @handle.register
#     def _(self, command: SettleUnit) -> None:
#         self.settle_unit_handler.handle(command)

#     @handle.register
#     def _(self, command: TrainUnit) -> None:
#         self.train_unit_handler.handle(command)




