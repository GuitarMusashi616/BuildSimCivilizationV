# pyright: strict

from abc import ABC, abstractmethod

class IQueue(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Gets the name of what is being queued up"""

    @property
    @abstractmethod
    def hammers_req(self) -> int:
        """Returns how many production hammers total to produce this"""

