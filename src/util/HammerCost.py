# pyright: strict

from unit.UnitType import UnitType


class HammerCost:
    @staticmethod
    def hammers_req_for_unit(unit: UnitType) -> int:
        if unit == UnitType.SETTLER:
            return 50
        
        if unit == UnitType.WARRIOR:
            return 26

        assert False, f"Could not get hammers req for {unit}"
    
    # @staticmethod
    # def hammers_req_for_building(building: BuildingType):
    #     pass

# hammer_cost = {
#     'worker': 46,
#     'scout': 16,
#     'warrior': 26,
#     'monument': 26
# }