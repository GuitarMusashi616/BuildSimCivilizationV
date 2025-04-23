# pyright: strict

import sqlite3

class Building:
    """Returns values associated with a building by wrapping a name like 'BUILDING_MONUMENT' and searching the database"""

    db_path = 'resources/Civ5CoreDatabase.db'

    def __init__(self, name: str):
        self.name = name
        self.conn = sqlite3.connect(Building.db_path)
        self.cursor = self.conn.cursor()

    def get_cost(self) -> int:
        # self.cursor.execute('select ')
        self.cursor.execute(f"select cost from Buildings where type = '{self.name}'")
        row = self.cursor.fetchone()
        assert row is not None, f"{self.name} could not be identified"
        return int(row[0])


if __name__ == "__main__":
    building = Building('BUILDING_MONUMENT')
    print(building.get_cost())