# pyright: strict

from queueable.IQueue import IQueue
from dataclasses import dataclass


@dataclass
class Building(IQueue):
    name: str
    hammers_req: int
    culture: int
    defense: float
    gold: int
    science: int
    prod: int
    great_work_art_slots: int
    food: int
    faith: int

    def get_hammers_req(self) -> int:
        return self.hammers_req