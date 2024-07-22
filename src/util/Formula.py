# pyright: strict

import math


GAME_SPEED_MULT = 1.5  # quick speed (normal is 1)
MAP_SIZE_MODIFIER = 0.3 # 0.2 for large, 0.15 for huge, (0.3 for everything else)

class Formula:
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
    def _base_culture_required_for_social_policy(num_policies: int) -> float:
        return (25+6*num_policies) / GAME_SPEED_MULT

    @staticmethod
    def _social_policy_cost_factor(num_cities: int) -> float:
        return 1 + MAP_SIZE_MODIFIER*(num_cities-1)

    @staticmethod
    def _round_down_to_mult_of_5(value: float) -> int:
        return 5 * math.floor(value/5)