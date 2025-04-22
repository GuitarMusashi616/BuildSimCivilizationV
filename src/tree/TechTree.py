# pyright: strict

from typing import List
# from researchable.Tech import Tech
import sqlite3
# from pathlib import Path


class TechTree:
    """Make a tech tree out of the Civ 5 Core Database"""
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.techs_researched: List[str] = []
    
    def research(self, tech: str):
        """Counts that tech as researched"""
        self.techs_researched.append(tech)

    def get_options(self) -> List[str]:
        """Returns the techs available to research"""
        placeholders = ','.join(['(?)'] * len(self.techs_researched))
        query = f"""
            WITH researched(tech) AS (
            VALUES {placeholders}
            ),

            prereq_status AS (
            SELECT  t.TechType,
                    COUNT(*)                           AS prereq_total,
                    SUM(CASE WHEN r.tech IS NOT NULL
                            THEN 1 ELSE 0 END)        AS prereq_satisfied
            FROM      Technology_PrereqTechs AS t
            LEFT JOIN researched  AS r
                    ON r.tech = t.PrereqTech
            GROUP BY  t.TechType
            )

            SELECT  TechType
            FROM    prereq_status
            WHERE   prereq_total = prereq_satisfied
            AND   TechType NOT IN (SELECT tech FROM researched);
        """
        self.cursor.execute(query, self.techs_researched)
        result: List[str] = []
        for row in self.cursor.fetchall():
            result.append(row[0])
        return result


if __name__ == "__main__":
    db_path = 'resources/Civ5CoreDatabase.db'
    # for item in Path('resources').iterdir():
    #     print(item)
    tree = TechTree(db_path)
    tree.research("TECH_AGRICULTURE")
    options = tree.get_options()
    while options:
        for i in range(1, len(options) + 1):
            print(f"{i}) {options[i-1]}")
        print()
        choice = int(input("Choose which tech to research: "))
        tree.research(options[choice-1])
        options = tree.get_options()


