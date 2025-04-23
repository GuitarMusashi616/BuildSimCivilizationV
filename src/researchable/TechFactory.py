from typing import List
from researchable.ITechDB import ITechDB
from researchable.Tech import Tech


class TechFactory:
    def __init__(self, tech_db: ITechDB):
        self.tech_db = tech_db

    def from_string(self, tech: str) -> Tech:
        cost = self.tech_db.get_cost(tech)
        return Tech(tech, cost)

    def from_string_list(self, techs: List[str]) -> List[Tech]:
        return [self.from_string(x) for x in techs]

    @staticmethod
    def pottery():
        return Tech('Pottery', 35)

    @staticmethod
    def writing():
        return Tech('Writing', 55)
    
