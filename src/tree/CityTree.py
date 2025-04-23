# pyright: strict

from typing import List
import sqlite3


class CityTree:
    """The buildings and units that the city can build"""
    def __init__(self, db_path: str):
        self.techs: List[str] = []
        self.buildings: List[str] = []
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def research(self, tech: str):
        self.techs.append(tech)
    
    def build(self, building: str):
        self.buildings.append(building)
    
    def get_options(self) -> List[str]:
        tech_placeholders = ['?'] * len(self.techs)
        building_placeholders = ['?'] * len(self.buildings)
        query = f"select Type, PrereqTech from Buildings where (PrereqTech is NULL or PrereqTech in ({', '.join(tech_placeholders)})) and (Type not in ({', '.join(building_placeholders)}))"
        self.cursor.execute(query, self.techs + self.buildings)
        return [x[0] for x in self.cursor.fetchall()]

def test():
    tree = CityTree('resources/Civ5CoreDatabase.db')
    tree.research('TECH_CALENDAR')
    tree.build('BUILDING_MONUMENT')
    print(tree.get_options())

if __name__ == "__main__":
    test()