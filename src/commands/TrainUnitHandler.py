from commands.TrainUnit import TrainUnit
from queueable.QueuedUnitFactory import QueuedUnitFactory
from repositories.CivRepo import CivRepo


class TrainUnitHandler:
    def __init__(self, civ_repo: CivRepo, unit_factory: QueuedUnitFactory):
        self.civ_repo = civ_repo
        self.unit_factory = unit_factory

    def handle(self, command: TrainUnit):
        civ = self.civ_repo.get(command.civ_id)
        city = civ.get_city(command.city_id)

        unit = self.unit_factory.spawn(command.unit_type)
        city.queue_up(unit)
        