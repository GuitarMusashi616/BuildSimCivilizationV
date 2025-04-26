# pyright: strict

from __future__ import annotations
from abc import ABC, abstractmethod

from adapter.ICityMadeListener import ICityMadeListener
from adapter.IUnitMadeListener import IUnitMadeListener
from unit.IUnit import IUnit


class ICiv(ABC):
    @abstractmethod
    def add_unit(self, unit: IUnit):
        pass

    @abstractmethod
    def add_unit_made_listener(self, listener: IUnitMadeListener):
        pass

    @abstractmethod
    def add_city_made_listener(self, listener: ICityMadeListener):
        pass
    
