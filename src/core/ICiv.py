# pyright: strict

from abc import ABC, abstractmethod

from unit.IUnit import IUnit


class ICiv(ABC):
    @abstractmethod
    def add_unit(self, unit: IUnit):
        pass
    
