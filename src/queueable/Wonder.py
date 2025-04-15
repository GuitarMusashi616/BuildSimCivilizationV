from queueable.IQueue import IQueue

class Wonder(IQueue):
    def __init__(self, name: str, culture: int, defense: float, gold: int, science: int, prod: int, great_work_art_slots: int, food: int, faith: int, hammers_req: int):
        self._name = name
        self.culture = culture
        self.defense = defense
        self.gold = gold
        self.science = science
        self.prod = prod
        self.great_work_art_slots = great_work_art_slots
        self.food = food
        self.faith = faith
        self._hammers_req = hammers_req
    
    def __repr__(self):
        return f"{self.name}({self.hammers_req})"
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def hammers_req(self) -> int:
        return self._hammers_req