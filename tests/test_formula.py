import unittest

from src.util.Formula import Formula

class TestFormula(unittest.TestCase):
    def test_damage_calculator(self):
        stronger_dmg, weaker_dmg = Formula.damage_calculator(25, 21)
        self.assertEqual(round(stronger_dmg), 33)
        self.assertEqual(round(weaker_dmg), 27)
    
    def test_wounded_cs(self):
        half = Formula.combat_strength_for_wounded(50, 30)
        lowest = Formula.combat_strength_for_wounded(1, 30)
        self.assertEqual(half, 25)
        self.assertEqual(lowest, 20)


if __name__ == "__main__":
    unittest.main()