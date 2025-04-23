# pyright: strict

from abc import ABC, abstractmethod

class IBuilding(ABC):
    @property
    @abstractmethod
    def food(self) -> int:
        pass

    @property
    @abstractmethod
    def prod(self) -> int:
        pass

    @property
    @abstractmethod
    def gold(self) -> int:
        pass

    @property
    @abstractmethod
    def science(self) -> int:
        pass

    @property
    @abstractmethod
    def culture(self) -> int:
        pass

    @property
    @abstractmethod
    def faith(self) -> int:
        pass