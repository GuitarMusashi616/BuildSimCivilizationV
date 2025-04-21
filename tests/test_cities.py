# pyright: basic

import unittest


class TestCities(unittest.TestCase):
    # Test if the growth, hammers works like when you lock growth it makes the next citizen born go straight to max hammers which applies immediately
    def test_hammers_after_growth(self):
        pass

    # Check if the civ is progressing science research
    def test_science_research(self):
        pass
    
if __name__ == "__main__":
    unittest.main()