# pyright: strict

import math
import sqlite3
from typing import Dict

from building.IBuildingDB import IBuildingDB
from tile.TileOutput import TileOutput

class BuildingDB(IBuildingDB):
    """Returns values associated with a building by wrapping a name like 'BUILDING_MONUMENT' and searching the database"""

    def __init__(self, db_path: str = 'resources/Civ5CoreDatabase.db', game_speed_mult: float = 2/3):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.game_speed_mult = game_speed_mult

    def get_cost(self, building: str) -> int:
        self.cursor.execute(f"select cost from Buildings where type = ?", (building,))
        row = self.cursor.fetchone()
        assert row is not None, f"{building} could not be identified"
        return math.floor(int(row[0]) * self.game_speed_mult)
    
    def get_yield_changes(self, building: str) -> TileOutput:
        self.cursor.execute(f"select YieldType, Yield from Building_YieldChanges where BuildingType = ?", (building,))
        rows = self.cursor.fetchall()
        assert bool(rows), f"{building} could not be identified"

        dic: Dict[str, int] = {}
        for row in rows:
            dic[row[0]] = row[1]

        return TileOutput.from_yield(dic)
    
    def get_yields(self, building: str) -> TileOutput:
        """Get all yield changes minus the gold per turn for maintenance"""
        yield_changes = self.get_yield_changes(building)
        yield_changes.gold -= self.get_maintenance(building)

        return yield_changes

    def get_maintenance(self, building: str) -> int:
        """Get the gpt maintenance cost of a building"""
        self.cursor.execute("select GoldMaintenance from Buildings where Type = ?", (building,))
        row = self.cursor.fetchone()
        assert row, f"Could not get maintenance for building: {building}"
        return int(row[0])
        


    
    def get_resource_yield_changes(self, building: str) -> Dict[str, TileOutput]:
        self.cursor.execute(f"select ResourceType, YieldType, Yield from Building_ResourceYieldChanges where BuildingType = ?", (building,))
        rows = self.cursor.fetchall()

        output: Dict[str, TileOutput] = {}
        dic: Dict[str, Dict[str, int]] = {}

        for row in rows:
            if not row[0] in dic:
                dic[row[0]] = {}

            dic[row[0]][row[1]] = row[2]
        
        for resource in dic:
            output[resource] = TileOutput.from_yield(dic[resource])
        
        return output
        

        





if __name__ == "__main__":
    buildingDB = BuildingDB('resources/Civ5coreDatabase.db')
    print(buildingDB.get_cost('BUILDING_MONUMENT'))
    print(buildingDB.get_yields('BUILDING_MONUMENT'))
    print(buildingDB.get_yields('BUILDING_WATERMILL'))