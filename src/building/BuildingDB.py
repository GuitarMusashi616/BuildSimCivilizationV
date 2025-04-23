# pyright: strict

import sqlite3
from typing import Dict

from building.IBuildingDB import IBuildingDB
from tile.TileOutput import TileOutput

class BuildingDB(IBuildingDB):
    """Returns values associated with a building by wrapping a name like 'BUILDING_MONUMENT' and searching the database"""

    def __init__(self, db_path: str = 'resources/Civ5CoreDatabase.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_cost(self, building: str) -> int:
        self.cursor.execute(f"select cost from Buildings where type = ?", (building,))
        row = self.cursor.fetchone()
        assert row is not None, f"{building} could not be identified"
        return int(row[0])
    
    def get_yields(self, building: str) -> TileOutput:
        self.cursor.execute(f"select YieldType, Yield from Building_YieldChanges where BuildingType = ?", (building,))
        rows = self.cursor.fetchall()
        assert bool(rows), f"{building} could not be identified"

        dic: Dict[str, int] = {}
        for row in rows:
            dic[row[0]] = row[1]

        return TileOutput.from_yield(dic)





if __name__ == "__main__":
    buildingDB = BuildingDB('resources/Civ5coreDatabase.db')
    print(buildingDB.get_cost('BUILDING_MONUMENT'))
    print(buildingDB.get_yields('BUILDING_MONUMENT'))