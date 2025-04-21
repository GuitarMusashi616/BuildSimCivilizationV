# pyright: strict
from __future__ import annotations
from abc import ABC, abstractmethod

from unit.IUnit import IUnit


class IUnitMadeListener(ABC):
    @abstractmethod
    def notify(self, unit: IUnit):
        pass