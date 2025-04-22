# pyright: strict

from abc import ABC, abstractmethod
from typing import List
from researchable.Tech import Tech

class ITechTree(ABC):
    """Returns techs based on what's available to research"""

    @abstractmethod
    def research(self, tech: Tech):
        """Counts that tech as researched"""
    
    @abstractmethod
    def get_options(self) -> List[Tech]:
        """Returns the techs available to research"""