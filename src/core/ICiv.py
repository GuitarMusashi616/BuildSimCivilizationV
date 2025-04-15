# pyright: strict

from abc import ABC, abstractmethod

from queueable.Unit import Unit

class ICiv(ABC):
    @abstractmethod
    def add_unit(self, unit: Unit):
        pass
    
