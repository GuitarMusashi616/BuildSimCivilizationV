from queueable.BuildingFactory import BuildingFactory
from core.City import City
from core.Civ import Civ
from enums.Nation import Nation
from researchable.PolicyFactory import PolicyFactory
from researchable.Tech import Tech
from researchable.TechFactory import TechFactory
from tile.Tile import Tile
from tile.TileFactory import TileFactory
from queueable.UnitFactory import UnitFactory
from queueable.WonderFactory import WonderFactory

def test():
    base = [
        TileFactory.grassland_river_city(),
        TileFactory.grassland_hill(),
        TileFactory.forest_grassland(),
        TileFactory.grassland_river(),
        TileFactory.grassland_river(),
        TileFactory.plains_river(),
        TileFactory.grassland_river_stone(),
    ]


    civ1 = Civ(Nation.BABYLON)
    civ2 = Civ(Nation.ARABIA)
    city1 = City(base)
    city1.pop = 5
    city2 = City(base)
    city2.pop = 7

    civ1.add_city(city1)
    civ1.add_city(city2)
    civ2.add_city(City(base))

    print([x.pop for x in civ1.cities])
    print([x.pop for x in civ2.cities])


    a = Tile(2, 2, 0, False)
    b = Tile(0, 2, 0, True)

    print(a.__dict__)
    print(b.__dict__)


def babylon_race():
    """Rush building the great library as babylon, show what happens every turn"""

    build_order_capital = [UnitFactory.worker(), BuildingFactory.granary(), WonderFactory.great_library()]
    build_order_tech = [TechFactory.pottery(), TechFactory.writing()]
    build_order_policy = [PolicyFactory.oligarchy()]

    base = [
        TileFactory.grassland_river_city(),
        TileFactory.grassland_hill(),
        TileFactory.forest_grassland(),
        TileFactory.grassland_river(),
        TileFactory.grassland_river(),
        TileFactory.plains_river(),
        TileFactory.grassland_river_stone(),
    ]

    civ = Civ(Nation.BABYLON)  # found city turn 1

    capital = City(base)
    capital.add_wonder(WonderFactory.palace())
    capital.pick_tiles([0, 6])
    capital.queue_up_many(build_order_capital)

    civ.add_city(capital)