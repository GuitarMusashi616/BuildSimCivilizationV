# pyright: strict

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from adapter.ICityMadeListener import ICityMadeListener
from adapter.IUnitMadeListener import IUnitMadeListener
from core.ICity import ICity
from tile.ITile import ITile
from unit.IUnit import IUnit


class ICiv(ABC):
    @abstractmethod
    def add_unit(self, unit: IUnit):
        pass

    @abstractmethod
    def get_unit(self, unit_id: int) -> IUnit:
        pass

    @abstractmethod
    def get_city(self, city_id: int) -> ICity:
        pass

    @abstractmethod
    def remove_unit(self, unitId: int):
        pass

    @abstractmethod
    def create_city(self, tiles: List[ITile], num_starting_tiles: int=7) -> ICity:
        pass

    @abstractmethod
    def add_unit_made_listener(self, listener: IUnitMadeListener):
        pass

    @abstractmethod
    def add_city_made_listener(self, listener: ICityMadeListener):
        pass
