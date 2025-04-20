# pyright: strict


from queueable.Building import Building


class BuildingFactory:
    @staticmethod
    def granary():
        return Building(
            name = 'Granary',
            hammers_req = 60,
            culture = 0,
            defense = 0,
            gold = 0,
            science = 0,
            prod = 0,
            great_work_art_slots = 0,
            food = 2,
            faith = 0,
        )
        
    @staticmethod
    def library():
        return Building(
            name = 'Library',
            hammers_req = 75,
            culture = 0,
            defense = 0,
            gold = -1,
            science = 0,
            prod = 0,
            great_work_art_slots = 0,
            food = 2,
            faith = 0,
        )