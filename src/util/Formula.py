# pyright: strict

import math
from typing import Tuple


GAME_SPEED_MULT = 1.5  # quick speed (normal is 1)
MAP_SIZE_MODIFIER = 0.3 # 0.2 for large, 0.15 for huge, (0.3 for everything else)

class Formula:
    """Formulas based on https://civilization.fandom.com/wiki/Mathematics_of_Civilization_V"""

    @staticmethod
    def food_required_to_grow(city_pop: int) -> int:
        # 1.5 at the end is the quick speed multiplier
        return (15 + 8*(city_pop-1) + (city_pop-1)**1.5) / GAME_SPEED_MULT

    @staticmethod
    def culture_required_for_border_growth(num_city_tiles: int) -> int:
        return (20 + (10 * (num_city_tiles-1))**1.1) / 2

    @staticmethod
    def culture_required_for_social_policy(num_policies: int, num_cities: int) -> float:
        return Formula._round_down_to_mult_of_5(Formula._base_culture_required_for_social_policy(num_policies) * Formula._social_policy_cost_factor(num_cities))

    @staticmethod
    def damage_calculator(cs_stronger_unit: int, cs_weaker_unit: int) -> Tuple[float, float]:
        # assume that it doesn't matter who initiates the battle
        x = cs_stronger_unit / cs_weaker_unit
        stronger_damage = ((((x+3)/4)**4)+1)/2
        weaker_damage = stronger_damage**-1
        return stronger_damage*30, weaker_damage*30

    @staticmethod
    def combat_strength_percentage_based_on_health(hp_fraction: float) -> float:
        # 20% means 20% higher than .666

        highest = 1
        lowest = .666

        diff = highest-lowest
        return lowest + diff*hp_fraction
    
    @staticmethod
    def combat_strength_for_wounded(hp: int, cs: int) -> float:
        """Assuming unit has 100 hp max"""
        return round(Formula.combat_strength_percentage_based_on_health(hp/100)*cs)


    # Private functions

    @staticmethod
    def _base_culture_required_for_social_policy(num_policies: int) -> float:
        return (25+6*num_policies) / GAME_SPEED_MULT

    @staticmethod
    def _social_policy_cost_factor(num_cities: int) -> float:
        return 1 + MAP_SIZE_MODIFIER*(num_cities-1)

    @staticmethod
    def _round_down_to_mult_of_5(value: float) -> int:
        return 5 * math.floor(value/5)
