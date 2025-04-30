# pyright: strict

import math


class OtherFormula:
    """Holds other alternative versions of formula not currently in use"""


    @staticmethod
    def culture_required_for_social_policy(
        num_policies_bought: int,
        num_cities: int,
        increase_per_city: float,
        per_city_discount: float,
    ) -> int:
        """
        Increase per city varies from 10% to 5% depending on map size
        perCityDiscount is 33% for civs with Representation
        https://civilization.fandom.com/wiki/Social_policies_(Civ5)#Cost"""
        base_cost = (3*num_policies_bought)**2.01 + 25
        additional_cost = base_cost * increase_per_city * (num_cities - 1) * (1 - per_city_discount)

        return OtherFormula.rounded_down_to_nearest_5(additional_cost)
    
    @staticmethod
    def rounded_down_to_nearest_5(value: float) -> int:
        return 5 * math.floor(value/5)

    @staticmethod
    def formula_for_social_policy_cost(
        num_policies: int,
        num_cities: int,
        game_speed_modifier: float,
        difficulty_coefficient: float,
        map_size_modifier: float,
    ) -> int:
        """
        Game speed modifier (3 for marathon, 1.5 for epic, 1 for normal, 0.67 for quick)
        Difficulty coefficient (0.5 for settler, 0.67 for chieftain, 0.85 for warlord, 1 otherwise)
        Map size modifier (0.3 for normal size and below, 0.2 for large, 0.15 for huge)
        
        https://civilization.fandom.com/wiki/Mathematics_of_Civilization_V#Calculating_Culture"""

        base_cost = game_speed_modifier * difficulty_coefficient * (25 + (6*num_policies) ** 1.7)
        cost_factor = 1 + map_size_modifier * (num_cities - 1)
        return OtherFormula.rounded_down_to_nearest_5(base_cost * cost_factor)


def test_diagonal_table():
    for k, n in zip(range(51), range(1, 30)):
        print((k, n), ": ", OtherFormula.formula_for_social_policy_cost(k, n, 1, 1, 0.3))


if __name__ == "__main__":


