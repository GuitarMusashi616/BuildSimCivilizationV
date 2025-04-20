# pyright: strict

from __future__ import annotations
from enum import Enum, auto

from tile.TileOutput import TileOutput


class ResourceType(Enum):
    RESOURCE_IRON = auto()
    RESOURCE_HORSE = auto()
    RESOURCE_COAL = auto()
    RESOURCE_OIL = auto()
    RESOURCE_ALUMINUM = auto()
    RESOURCE_URANIUM = auto()
    RESOURCE_WHEAT = auto()
    RESOURCE_COW = auto()
    RESOURCE_SHEEP = auto()
    RESOURCE_DEER = auto()
    RESOURCE_BANANA = auto()
    RESOURCE_FISH = auto()
    RESOURCE_STONE = auto()
    RESOURCE_WHALE = auto()
    RESOURCE_PEARLS = auto()
    RESOURCE_GOLD = auto()
    RESOURCE_SILVER = auto()
    RESOURCE_GEMS = auto()
    RESOURCE_MARBLE = auto()
    RESOURCE_IVORY = auto()
    RESOURCE_FUR = auto()
    RESOURCE_DYE = auto()
    RESOURCE_SPICES = auto()
    RESOURCE_SILK = auto()
    RESOURCE_SUGAR = auto()
    RESOURCE_COTTON = auto()
    RESOURCE_WINE = auto()
    RESOURCE_INCENSE = auto()
    RESOURCE_JEWELRY = auto()
    RESOURCE_PORCELAIN = auto()
    RESOURCE_COPPER = auto()
    RESOURCE_SALT = auto()
    RESOURCE_CRAB = auto()
    RESOURCE_TRUFFLES = auto()
    RESOURCE_CITRUS = auto()
    RESOURCE_ARTIFACTS = auto()
    RESOURCE_NUTMEG = auto()
    RESOURCE_CLOVES = auto()
    RESOURCE_PEPPER = auto()
    RESOURCE_HIDDEN_ARTIFACTS = auto()
    RESOURCE_BISON = auto()
    RESOURCE_COCO = auto()

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

        