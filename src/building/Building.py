# pyright: strict

from building.IBuilding import IBuilding
from tile.TileOutput import TileOutput


class Building(IBuilding):
    def __init__(self, name: str, output: TileOutput):
        self.name = name
        self.output = output

    @property
    def food(self) -> int:
        return self.output.food

    @property
    def prod(self) -> int:
        return self.output.prod

    @property
    def gold(self) -> int:
        return self.output.gold

    @property
    def science(self) -> int:
        return self.output.science

    @property
    def culture(self) -> int:
        return self.output.culture

    @property
    def faith(self) -> int:
        return self.output.faith
    