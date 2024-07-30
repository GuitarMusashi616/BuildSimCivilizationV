# pyright: strict

from commands.SpawnCity import SpawnCity
from core.CityFactory import CityFactory
from repositories.CivRepo import CivRepo
from tile.TileFactory import TileFactory


class SpawnCityHandler:
    def __init__(self, civ_repo: CivRepo, city_factory: CityFactory):
        self.civ_repo = civ_repo
        self.city_factory = city_factory

    def handle(self, command: SpawnCity):
        civ = self.civ_repo.get(command.civ_id)
        city = None

        base = [
            TileFactory.grassland_river_city(),
            TileFactory.grassland_hill(),
            TileFactory.forest_grassland(),
            TileFactory.grassland_river(),
            TileFactory.grassland_river(),
            TileFactory.plains_river(),
            TileFactory.grassland_river_stone(),

            TileFactory.grassland_hill(),
            TileFactory.forest_grassland(),
            TileFactory.grassland_river(),
            TileFactory.grassland_river(),
            TileFactory.plains_river(),
            TileFactory.grassland_river_stone(),
        ]


        if civ.num_cities == 0:
            city = self.city_factory.capital(base)
        else:
            city = self.city_factory.city(base)

        assert city, "Error instantiating city"

        civ.add_city(city, command.city_id)
    
        return city


