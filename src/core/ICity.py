# pyright: strict

from abc import ABC, abstractmethod
from typing import List

from queueable.IQueue import IQueue

class ICity(ABC):
    @property
    @abstractmethod
    def id(self) -> int:
        """Returns the entity's id"""

    @abstractmethod
    def next_turn(self):
        """Simulates the next turn of the city"""

    @abstractmethod
    def stats(self):
        """Prints the status of the city"""

    @abstractmethod
    def queue_up(self, iqueue: IQueue):
        pass

    @abstractmethod
    def queue_up_many(self, queue: List[IQueue]):
        pass
    
    @abstractmethod
    def get_gold(self) -> int:
        pass

    @abstractmethod
    def get_pop(self) -> int:
        pass

    @abstractmethod
    def get_science(self) -> int:
        pass

    @abstractmethod
    def get_culture(self) -> int:
        pass

    @abstractmethod
    def get_faith(self) -> int:
        pass

