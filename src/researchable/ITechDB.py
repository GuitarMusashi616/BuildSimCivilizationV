# pyright: strict

from abc import ABC, abstractmethod

class ITechDB(ABC):
    @abstractmethod
    def get_cost(self, tech: str) -> int:
        """Returns cost of tech"""