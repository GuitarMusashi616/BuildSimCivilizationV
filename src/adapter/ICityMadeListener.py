# pyright: strict
from __future__ import annotations
from abc import ABC, abstractmethod

from core.ICity import ICity


class ICityMadeListener(ABC):
    @abstractmethod
    def notify(self, city: ICity):
        pass