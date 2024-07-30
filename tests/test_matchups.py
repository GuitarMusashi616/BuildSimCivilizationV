import unittest

from src.util.Formula import Formula

class TestMatchups(unittest.TestCase):
    def test_vs_city(self):
        stronger_dmg, weaker_dmg = Formula.damage_calculator(25, 14)
        # print(stronger_dmg)
        # print(weaker_dmg)

        # self.assertEqual(round(stronger_dmg), 33)
        # self.assertEqual(round(weaker_dmg), 27)
        
        # usual city around 18 defense (no walls)
        # + 5 defense with walls (+50% with oligarchy)
        # therefore 25 defense, how many catapults required

        # catapult - 7 cs, 7 rs
        # trebechet - 12 cs, 14 cs
        # +200% damage to cities

        # catapult = 250 hp / 27 damage = 10 turns (so 3-4 turns with 3 catapults)
        # trebechet = 250 hp / 36 damage = 7 turns (so 2 turns with 3 trebechets)
    
        # catapult - 33 damage from city per turn - lasts 3 turns (1-shot if no city bonus (only when attacking?))
        # trebechet - 25 damage from city per turn - lasts 4 turns (2-3 shots if no city bonus) (30% bonus = 46 => 62)

        # archer - 5 cs, 7 rs
        # composite bowman - 7 cs, 11 rs
        # crossbow - 18 rs, 13 cs


if __name__ == "__main__":
    unittest.main()