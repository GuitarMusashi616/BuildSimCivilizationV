# pyright: strict

from __future__ import annotations
from enum import Enum, auto

from tile.TileOutput import TileOutput


class ResourceType(Enum):
    NONE = auto()
    CATTLE = auto()
    STONE = auto()
    SILVER = auto()

    @staticmethod
    def add_stats(resource: ResourceType) -> TileOutput:
        if resource == ResourceType.CATTLE:
            return TileOutput(
                food = 1,
                prod = 0,
                gold = 0,
                culture = 0,
                science = 0,
                faith = 0,
            )

        if resource == ResourceType.STONE:
            return TileOutput(
                food = 0,
                prod = 1,
                gold = 0,
                culture = 0,
                science = 0,
                faith = 0,
            )

        if resource == ResourceType.SILVER:
            return TileOutput(
                food = 0,
                prod = 0,
                gold = 2,
                culture = 0,
                science = 0,
                faith = 0,
            )

        return TileOutput(
            food = 0,
            prod = 0,
            gold = 0,
            culture = 0,
            science = 0,
            faith = 0,
        )

        