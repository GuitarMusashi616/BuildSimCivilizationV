# pyright: strict

from commands.NewCiv import NewCiv
from core.CivFactory import CivFactory
from repositories.CivRepo import CivRepo

class NewCivHandler:
    def __init__(self, civ_factory: CivFactory, civ_repo: CivRepo):
        self.civ_factory = civ_factory
        self.civ_repo = civ_repo

    def handle(self, command: NewCiv):
        civ = self.civ_factory.create(command.nation, command.settler_id)
        self.civ_repo.put(command.civ_id, civ)

