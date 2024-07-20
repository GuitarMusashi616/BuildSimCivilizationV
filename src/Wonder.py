from dataclasses import dataclass

@dataclass
class Wonder:
    culture: int
    defense: float
    gold: int
    science: int
    prod: int
    great_work_art_slots: int