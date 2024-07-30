# pyright: strict

from commands.DeleteUnit import DeleteUnit
from commands.DeleteUnitHandler import DeleteUnitHandler
from commands.SettleUnit import SettleUnit
from commands.SpawnCity import SpawnCity
from commands.SpawnCityHandler import SpawnCityHandler


class SettleUnitHandler:
    def __init__(self, delete_unit: DeleteUnitHandler, spawn_city: SpawnCityHandler):
        self.delete_unit = delete_unit
        self.spawn_city = spawn_city

    def handle(self, command: SettleUnit):
        self.delete_unit.handle(DeleteUnit(command.civ_id, command.unit_id))
        self.spawn_city.handle(SpawnCity(command.civ_id, command.new_city_id))
        