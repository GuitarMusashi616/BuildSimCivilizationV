# pyright: strict
from dataclasses import dataclass
# from typing import List

from queueable.IQueue import IQueue
# from queueable.UnitAction import UnitAction
from queueable.UnitType import UnitType

@dataclass
class Unit(IQueue):
    unit_type: UnitType
    hammers_req: int
    # action_queue: List[UnitAction]

    def next_turn(self):
        # affected by land
        pass

    def get_name(self) -> str: # type: ignore
        return self.unit_type.name

    def get_hammers_req(self) -> int:
        return self.hammers_req


    