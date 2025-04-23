# pyright: strict

from abc import ABC, abstractmethod

class IUnitDB(ABC):
    @abstractmethod
    def get_cost(self, unit: str) -> int:
        """Returns production/hammer cost of unit, errors if unit does not exist"""
