# pyright: strict

import sqlite3

from researchable.ITechDB import ITechDB

class TechDB(ITechDB):
    """Returns values associated with a tech by wrapping a name like 'TECH_POTTERY' and searching the database"""

    def __init__(self, db_path: str = 'resources/Civ5CoreDatabase.db', game_speed_mult: float = 2/3):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.game_speed_mult = game_speed_mult

    def get_cost(self, tech: str) -> int:
        self.cursor.execute(f"select cost from Technologies where type = ?", (tech,))
        row = self.cursor.fetchone()
        assert row is not None, f"{tech} could not be identified"
        number = int(row[0])
        return self._rounded_down_mult_of_5(number * self.game_speed_mult)
    
    def _rounded_down_mult_of_5(self, number: float) -> int:
        return round(number / 5) * 5


if __name__ == "__main__":
    techDB = TechDB('resources/Civ5coreDatabase.db')
    print(techDB.get_cost('TECH_POTTERY'))