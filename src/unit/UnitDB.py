# pyright: strict

import math
import sqlite3

from unit.IUnitDB import IUnitDB

class UnitDB(IUnitDB):
    """Returns values associated with a building by wrapping a name like 'BUILDING_MONUMENT' and searching the database"""

    def __init__(self, db_path: str = 'resources/Civ5CoreDatabase.db', game_speed_mult: float = 2/3):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.game_speed_mult = game_speed_mult

    def get_cost(self, unit: str) -> int:
        self.cursor.execute(f"select cost from Units where type = ?", (unit,))
        row = self.cursor.fetchone()
        assert row is not None, f"{unit} could not be identified"
        return math.floor(int(row[0]) * self.game_speed_mult)

if __name__ == "__main__":
    unitDB = UnitDB('resources/Civ5coreDatabase.db')
    print(unitDB.get_cost('UNIT_SCOUT'))