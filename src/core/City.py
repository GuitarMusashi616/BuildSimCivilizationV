# pyright: basic

import math
from typing import List
from queueable.IQueue import IQueue
from queueable.Wonder import Wonder
from tile.Tile import Tile
from queueable.Building import Building
from util.Formula import Formula
from queueable.Unit import Unit
from tile_strat.DefaultTileStrat import DefaultTileStrat
from tile_strat.IPickTileStrat import IPickTileStrat

class City:
    """Represents a city, make sure to also pick the tile the city is on!"""

    def __init__(self, tiles, num_starting_tiles=7):
        self.pop: int = 1
        self.food_acc: int = 0
        self.hammers_acc: int = 0
        self.culture_acc: int = 0

        self.tiles: List[Tile] = tiles[:num_starting_tiles]
        self.future_tiles: List[Tile] = tiles[num_starting_tiles:]
        self.tile_strat: IPickTileStrat = DefaultTileStrat()

        self.wonders: List[Wonder] = []
        self.buildings: List[Building] = []
        self.queue: List[IQueue] = []

    def reset_tiles(self):
        for tile in self.tiles:
            tile.is_worked = False
    
    def pick_tiles(self, indices: List[int]):
        for index in indices:
            self.tiles[index].is_worked = True

    def pick_tiles_with_strat(self):
        """Use selected tile strategy to pick which tiles to work"""
        self.reset_tiles()
        assert len(self.tiles) > 1, "City must have at least 2 tiles"
        indices = self.tile_strat.pick_tiles(self.tiles, self.pop)  # add 1 because it always works the first tile
        self.pick_tiles(indices)

    def set_tile_strat(self, tile_strat: IPickTileStrat):
        self.tile_strat = tile_strat
    
    def add_wonder(self, wonder: Wonder):
        self.wonders.append(wonder)

    def add_building(self, building: Building):
        self.buildings.append(building)

    def queue_up(self, iqueue: IQueue):
        self.queue.append(iqueue)

    def queue_up_many(self, queue: List[IQueue]):
        self.queue.extend(queue)

    def get_pop(self):
        return self.pop

    def get_prod(self):
        prod = 0
        for tile in self.tiles:
            if tile.is_worked:
                prod += tile.prod
        
        for wonder in self.wonders:
            prod += wonder.prod

        for building in self.buildings:
            prod += building.prod

        return prod

    def get_base_food(self):
        """Returns the base food before the existing population eats it"""
        food = 0
        for tile in self.tiles:
            if tile.is_worked:
                food += tile.food
        
        for wonder in self.wonders:
            food += wonder.food
        
        for building in self.buildings:
            food += building.food

        return food


    def get_food(self):
        """Returns the excess food"""
        return self.get_base_food() - self.pop*2

    def get_gold(self):
        gold = 0

        for tile in self.tiles:
            if tile.is_worked:
                gold += tile.gold

        for wonder in self.wonders:
            gold += wonder.gold

        for building in self.buildings:
            gold += building.gold

        return gold

    def get_science(self):
        science = 0

        for tile in self.tiles:
            if tile.is_worked:
                science += tile.science

        for wonder in self.wonders:
            science += wonder.science

        for building in self.buildings:
            science += building.science
        
        # add the 1st pop as a science
        # going to assume every pop adds +1 science
        science += self.pop

        return science

    def get_faith(self):
        faith = 0

        for tile in self.tiles:
            if tile.is_worked:
                faith += tile.faith

        for wonder in self.wonders:
            faith += wonder.faith

        for building in self.buildings:
            faith += building.faith
        
        return faith

    def get_tourism(self):
        return 0

    def get_culture(self):
        culture = 0

        for tile in self.tiles:
            if tile.is_worked:
                culture += tile.culture

        for wonder in self.wonders:
            culture += wonder.culture

        for building in self.buildings:
            culture += building.culture

        return culture

    def get_border_growth_culture_req(self):
        return round(Formula.culture_required_for_border_growth(len(self.tiles)-6))
    
    def get_border_growth_progress(self):
        try:
            return math.ceil((self.get_border_growth_culture_req() - self.culture_acc) / self.get_culture())
        except ZeroDivisionError:
            return -1

    def get_growth_progress(self) -> int:
        try:
            return math.ceil((Formula.food_required_to_grow(self.pop) - self.food_acc) / self.get_food())
        except ZeroDivisionError:
            return -1

    def get_prod_progress(self) -> int:
        try:
            return math.ceil((self.queue[0].get_hammers_req() - self.hammers_acc) / self.get_prod())
        except ZeroDivisionError:
            return -1

    def next_turn(self):
        self.food_acc += self.get_food()
        self.culture_acc += self.get_culture()
        self.hammers_acc += self.get_prod()

        # production complete
        if self.has_queued() and self.hammers_acc >= self.total_hammers_req():
            self.hammers_acc -= self.total_hammers_req()
            queueable = self.queue.pop(0)
            if isinstance(queueable, Wonder):
                self.add_wonder(queueable)

            if isinstance(queueable, Building):
                self.add_building(queueable)
        
        # growth
        food_req = Formula.food_required_to_grow(self.pop)
        if self.food_acc >= food_req:
            self.food_acc -= food_req
            self.pop += 1
            self.pick_tiles_with_strat()
        
        # culture
        culture_req = self.get_border_growth_culture_req()
        if self.culture_acc >= culture_req and self.future_tiles:
            self.culture_acc -= culture_req
            self.tiles.append(self.future_tiles.pop(0))


    def has_queued(self):
        """Returns whether this city has anything queued up in production"""
        return len(self.queue) > 0

    def total_hammers_req(self):
        """Returns the total production hammers required to complete current item, errors if nothing queued"""

        assert self.has_queued, "Nothing queued up"
        return self.queue[0].get_hammers_req()


        



    def stats(self):
        print(f'\tpop: {self.pop}')
        print(f'\tfood: {self.food_acc}/{Formula.food_required_to_grow(self.pop)} (+{self.get_food()}) [{self.get_growth_progress()} turns]')

        if len(self.queue) > 0:
            print(f'\tproduction: {self.hammers_acc}/{self.queue[0].get_hammers_req()} (+{self.get_prod()}) [{self.get_prod_progress()} turns]')
        else:
            print(f'\tproduction: +{self.get_prod()}')

        print(f'\tgold: +{self.get_gold()}')
        print(f'\tscience: +{self.get_science()}')
        print(f'\tfaith: +{self.get_faith()}')
        print(f'\ttourism: +{self.get_tourism()}')
        print(f'\tculture: {self.culture_acc}/{self.get_border_growth_culture_req()} (+{self.get_culture()}) [{self.get_border_growth_progress()} turns]')
        print()
        print(f'\tproduction queue: {self.queue}')


        # pop: 1, growth: 20/30 (+2) [5 turns]
        # prod: 'worker' 0/46 (+5) [10 turns]

        # gold: +3
        # science: +4
        # faith: +0
        # tourism: +0
        # culture: +1, border growth (0/10)

        # tiles: []
        # buildings: []
        # wonders: []
    

