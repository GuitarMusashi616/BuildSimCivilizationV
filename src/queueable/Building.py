# pyright: strict

from queueable.IQueue import IQueue

class Building(IQueue):
    def __init__(self, name: str, hammers_req: int, culture: int,
                  defense: float, gold: int, science: int, prod: int, great_work_art_slots: int, food: int, faith: int):
        self._name = name
        self._hammers_req = hammers_req
        self.culture = culture
        self.defense = defense
        self.gold = gold
        self.science = science
        self.prod = prod
        self.great_work_art_slots = great_work_art_slots
        self.food = food
        self.faith = faith

    def __repr__(self):
        return f"{self.name}({self.hammers_req})"

    @property
    def hammers_req(self) -> int:
        return self._hammers_req
    
    @property
    def name(self) -> str:
        return self._name