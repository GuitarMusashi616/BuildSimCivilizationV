# pyright: strict

from commands.DeleteUnit import DeleteUnit
from repositories.CivRepo import CivRepo


class DeleteUnitHandler:
    def __init__(self, civ_repo: CivRepo):
        self.civ_repo = civ_repo

    def handle(self, command: DeleteUnit):
        civ = self.civ_repo.get(command.civ_id)
        civ.remove_unit(command.unit_id)
