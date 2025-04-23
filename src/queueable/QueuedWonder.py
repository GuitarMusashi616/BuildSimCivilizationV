from building.IBuilding import IBuilding
from queueable.IQueue import IQueue

class QueuedWonder(IQueue, IBuilding):
    def __init__(self, name: str, culture: int, defense: float, gold: int, science: int, prod: int, great_work_art_slots: int, food: int, faith: int, hammers_req: int):
        self.defense = defense
        self.great_work_art_slots = great_work_art_slots
        self._name = name
        self._hammers_req = hammers_req
        self._culture = culture
        self._gold = gold
        self._science = science
        self._prod = prod
        self._food = food
        self._faith = faith
    
    def __repr__(self):
        return f"{self.name}({self.hammers_req})"
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def hammers_req(self) -> int:
        return self._hammers_req
    
    @property
    def food(self) -> int:
        return self._food

    @property
    def prod(self) -> int:
        return self._prod

    @property
    def science(self) -> int:
        return self._science

    @property
    def culture(self) -> int:
        return self._culture

    @property
    def faith(self) -> int:
        return self._faith

    @property
    def gold(self) -> int:
        return self._gold

    def instantiate(self) -> IBuilding:
        return self
