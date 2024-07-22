# pyright: basic

from queueable.Wonder import Wonder


class WonderFactory:
    @staticmethod
    def palace() -> Wonder:
        return Wonder(
            name='Palace',
            culture=1,
            defense=2.5,
            gold=3,
            science=3,
            prod=3,
            great_work_art_slots=1,
            food=0,
            faith=0,
            hammers_req=0,
        )

    @staticmethod
    def great_library():
        return Wonder(
            name='Great Library',
            culture=0,
            defense=0,
            gold=0,
            science=3,
            prod=0,
            great_work_art_slots=0,
            food=0,
            faith=0,
            hammers_req=0,
        )