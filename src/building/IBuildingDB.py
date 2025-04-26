# pyright: strict

from abc import ABC, abstractmethod
from typing import Dict

from tile.TileOutput import TileOutput

class IBuildingDB(ABC):
    @abstractmethod
    def get_cost(self, building: str) -> int:
        """Returns production/hammer cost of building, errors if building does not exist"""

    @abstractmethod
    def get_yields(self, building: str) -> TileOutput:
        """Returns the TileOutput yields like food and prod of a building"""

    @abstractmethod
    def get_resource_yield_changes(self, building: str) -> Dict[str, TileOutput]:
        """Returns Resource Yield Changes"""
