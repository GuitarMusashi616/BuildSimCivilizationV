from typing import List
from core.City import City
from queueable.WonderFactory import WonderFactory
from tile.ITile import ITile


class CityFactory:
    @staticmethod
    def capital(base: List[ITile]):
        capital = City(base)
        capital.add_wonder(WonderFactory.palace())
        capital.pick_tiles_with_strat()
        return capital

    @staticmethod
    def city(base: List[ITile]):
        city = City(base)
        city.pick_tiles_with_strat()
        return city

