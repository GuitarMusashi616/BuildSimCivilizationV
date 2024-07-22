from dataclasses import dataclass

from queueable.IQueue import IQueue

@dataclass
class Wonder(IQueue):
    name: str
    culture: int
    defense: float
    gold: int
    science: int
    prod: int
    great_work_art_slots: int
    food: int
    faith: int
    hammers_req: int

    def get_hammers_req(self) -> int:
        return self.hammers_req