# pyright: strict

from abc import ABC, abstractmethod

from tile.TileOutput import TileOutput

class IBuildingDB(ABC):
    @abstractmethod
    def get_cost(self, building: str) -> int:
        """Returns production/hammer cost of building, errors if building does not exist"""

    @abstractmethod
    def get_yields(self, building: str) -> TileOutput:
        """Returns the TileOutput yields like food and prod of a building"""