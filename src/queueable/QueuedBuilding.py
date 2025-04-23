# pyright: strict

from queueable.IQueue import IQueue


class QueuedBuilding(IQueue):
    def __init__(self, name: str, hammers_req: int):
        self._name = name
        self._hammers_req = hammers_req
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def hammers_req(self) -> int:
        return self._hammers_req

    def __repr__(self):
        return f"{self.name}({self.hammers_req})"
