# pyright: strict


from queueable.StaticQueuedBuilding import StaticQueuedBuilding


class QueuedBuildingFactory:
    @staticmethod
    def granary():
        return StaticQueuedBuilding(
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
        return StaticQueuedBuilding(
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