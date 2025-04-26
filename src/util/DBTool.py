# pyright: strict

import sqlite3

class DBTool:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    
    def all_fields_labeled(self, table: str, where_clause: str = ""):
        self.cursor.execute(f"pragma table_info({table})")
        columns = [desc[1] for desc in self.cursor.fetchall()]

        # self.cursor.execute(f"select * from {table} where Type = 'BUILDING_MONUMENT'")
        self.cursor.execute(f"select * from {table} {where_clause} limit 1")

        for row in self.cursor.fetchall():
            col_val_pairs = dict(zip(columns, row))
            for k,v in col_val_pairs.items():
                print(k,': ', v)

    def all_nonempty_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
        for row in self.cursor.fetchall():
            print(row)
        

def loop_queries():
    conn = sqlite3.connect('resources/Civ5CoreDatabase.db')
    cursor = conn.cursor()
    query = "something"
    while query:
        query = input("Query: ")
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
            print()

def query(query: str):
    conn = sqlite3.connect('resources/Civ5CoreDatabase.db')
    cursor = conn.cursor()
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
        print()

def tables_with_row_counts(filter: str=""):
    qstring = "SELECT tbl, stat FROM sqlite_stat1 WHERE idx IS NULL AND CAST(stat AS INTEGER)>0"
    if filter: 
        qstring += f" AND tbl like '%{filter}%'"
    query(qstring)

def update():
    conn = sqlite3.connect('resources/Civ5CoreDatabase.db')
    cursor = conn.cursor()
    query = "update units set cost = 106 where type = 'UNIT_SETTLER'"
    cursor.execute(query)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # tool = DBTool('resources/Civ5CoreDatabase.db')
    # tool.all_fields_labeled('Units', "where Type = 'UNIT_SETTLER'")

    # loop_queries()
    # tables_with_row_counts('yield')
    # query('select * from Building_ResourceYieldChanges')
    # query('pragma table_info(Building_ResourceYieldChanges)')

    query('select * from Resource_YieldChanges')
    query('pragma table_info(Resource_YieldChanges)')

    # query("select * from Building_YieldChanges where BuildingType like '%stone%'")
    # query('pragma table_info(GameSpeed_Turns)')
    # query("select * from GameSpeed_Turns")
    # science per 2 population
    # +1 happiness
    # +40% growth carried over
    # +25% gold

