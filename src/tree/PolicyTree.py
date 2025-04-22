# pyright: strict

from typing import List
# from researchable.Tech import Tech
import sqlite3
# from pathlib import Path


class PolicyTree:
    """Make a policy tree out of the Civ 5 Core Database"""
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.policies_researched: List[str] = []
    
    def research(self, policy: str):
        """Counts that policy as researched"""
        self.policies_researched.append(policy)

    def get_options(self) -> List[str]:
        """Returns the policies available to research"""
        placeholders = ','.join(['(?)'] * len(self.policies_researched))
        query = f"""
            /* ======  Set‑up: list the policies you HAVE researched  ====== */
            WITH researched(type) AS (         -- ← supply your list here
            VALUES {placeholders}
            ),

            /* ======  1.  Which policy branches are unlocked?  ====== */
            unlocked_branches AS (
            SELECT pbt.Type
            FROM   PolicyBranchTypes AS pbt
            JOIN   researched       AS r  ON r.type = pbt.FreePolicy
            ),

            /* ======  2.  Candidate policies (branch unlocked & not taken)  ====== */
            candidates AS (
            SELECT p.Type
            FROM   Policies AS p
            WHERE  p.Type NOT IN (SELECT type FROM researched) AND p.Type NOT LIKE '%FINISHER%'                   -- not researched yet
                AND (p.PolicyBranchType IS NULL                                    -- no branch needed
                    OR p.PolicyBranchType IN (SELECT Type FROM unlocked_branches))-- branch unlocked
            ),

            /* ======  3.  Keep only policies whose *every* prerequisite is done  ====== */
            eligible AS (
            SELECT  c.Type
            FROM    candidates            AS c
            LEFT    JOIN Policy_PrereqPolicies AS pp  ON pp.PolicyType  = c.Type
            LEFT    JOIN researched            AS r2 ON r2.type        = pp.PrereqPolicy
            GROUP BY c.Type
            HAVING  COUNT(pp.PrereqPolicy) = COUNT(r2.type)  -- 0 = 0 ⇒ handles “no‑prereq” cases too
            )

            /* ======  Final result  ====== */
            SELECT Type AS ResearchablePolicy
            FROM   eligible
            ORDER  BY Type;
        """
        self.cursor.execute(query, self.policies_researched)
        result: List[str] = []
        for row in self.cursor.fetchall():
            result.append(row[0])
        return result


if __name__ == "__main__":
    db_path = 'resources/Civ5CoreDatabase.db'
    # for item in Path('resources').iterdir():
    #     print(item)
    tree = PolicyTree(db_path)
    tree.research("TECH_AGRICULTURE")
    options = tree.get_options()
    while options:
        for i in range(1, len(options) + 1):
            print(f"{i}) {options[i-1]}")
        print()
        choice = int(input("Choose which policy to research: "))
        tree.research(options[choice-1])
        options = tree.get_options()




