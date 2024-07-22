# pyright: strict
from dataclasses import dataclass

from queueable.IQueue import IQueue

@dataclass
class Unit(IQueue):
    name: str
    hammers_req: int

    def get_hammers_req(self) -> int:
        return self.hammers_req


    