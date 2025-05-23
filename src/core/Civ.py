# pyright: strict

from __future__ import annotations
import math
from typing import Dict, List
from adapter.ICityMadeListener import ICityMadeListener
from adapter.IUnitMadeListener import IUnitMadeListener
from building.IBuildingFactory import IBuildingFactory
from core.City import City
from core.ICity import ICity
from core.ICiv import ICiv
from tile.ITile import ITile
from unit.IUnitFactory import IUnitFactory
from util.Formula import Formula
from enums.Nation import Nation
from researchable.Policy import Policy
from researchable.Tech import Tech
from unit.IUnit import IUnit

STARTING_HAPPINESS = 9

class Civ(ICiv):
    def __init__(self, nation: Nation, building_factory: IBuildingFactory, unit_factory: IUnitFactory):
        self.building_factory = building_factory
        self.unit_factory = unit_factory

        self.nation = nation

        self.tech_queue: List[Tech] = []
        self.researched: List[Tech] = []
        self.social_policies_queue: List[Policy] = []
        self.social_policies: List[Policy] = []

        self.cities: Dict[int, ICity] = {}
        self.units: Dict[int, IUnit] = {}
        self.units_to_remove: List[int] = []

        self.gold_acc = 0
        self.science_acc = 0
        self.culture_acc = 0
        self.faith_acc = 0
        self.happiness_acc = 0
        
        self.unit_made_listeners: List[IUnitMadeListener] = []
        self.city_made_listeners: List[ICityMadeListener] = []

    @property
    def num_cities(self):
        return len(self.cities)

    def queue_tech(self, tech: Tech):
        self.tech_queue.append(tech)

    def queue_many_tech(self, tech: List[Tech]):
        self.tech_queue.extend(tech)

    def queue_policy(self, policy: Policy):
        self.social_policies_queue.append(policy)

    def queue_many_policy(self, policy: List[Policy]):
        self.social_policies_queue.extend(policy)
    
    def _add_city(self, city: ICity):
        self.cities[city.id] = city
        for listener in self.city_made_listeners:
            listener.notify(city)
    
    def create_city(self, tiles: List[ITile], num_starting_tiles: int=7) -> ICity:
        is_capital = len(self.cities) < 1
        city = City(self.building_factory, self.unit_factory, tiles, self, num_starting_tiles, is_capital)
        self._add_city(city)
        return city
    
    def get_city(self, city_id: int) -> ICity:
        assert city_id in self.cities, f"City with city_id: {city_id} does not exist"
        return self.cities[city_id]

    def add_unit(self, unit: IUnit):
        self.units[unit.id] = unit
        for listener in self.unit_made_listeners:
            listener.notify(unit)
    
    def get_unit(self, unit_id: int) -> IUnit:
        return self.units[unit_id]
    
    def remove_unit(self, unitId: int):
        """Just queue the removal of a unit"""
        self.units_to_remove.append(unitId)
    
    def _remove_unit(self, unitId: int):
        # assert 0 <= unitId < len(self.units), f"Cannot remove unitId: {unitId}"
        assert self.units[unitId], f"Unit with unitId: {unitId} cannot be deleted"
        del self.units[unitId]
    
    def cleanup_units(self):
        while self.units_to_remove:
            unitId = self.units_to_remove.pop()
            self._remove_unit(unitId)

    def get_gold(self):
        return sum(x.get_gold() for x in self.cities.values())

    def get_positive_happiness(self):
        return STARTING_HAPPINESS

    def get_total_pop(self):
        return sum(x.get_pop() for x in self.cities.values())

    def get_negative_happiness(self):
        return len(self.cities)*3 + self.get_total_pop()

    def get_happiness(self):
        return self.get_positive_happiness() - self.get_negative_happiness()

    def get_science(self):
        return sum(x.get_science() for x in self.cities.values())

    def get_culture(self):
        return sum(x.get_culture() for x in self.cities.values())

    def get_faith(self):
        return sum(x.get_faith() for x in self.cities.values())

    def get_research_progress(self):
        try:
            return math.ceil((self.tech_queue[0].science - self.science_acc) / self.get_science())
        except ZeroDivisionError:
            return -1

    def get_social_policy_culture_req(self):
        return Formula.culture_required_for_social_policy(len(self.social_policies), len(self.cities.values()))

    def get_social_policy_progress(self):
        try:
            return math.ceil((self.get_social_policy_culture_req() - self.culture_acc) / self.get_culture())
        except ZeroDivisionError:
            return -1

    def stats(self):
        print("CIVILIZATON STATS")
        if len(self.tech_queue) > 0:
            print(f'\tscience: {self.science_acc}/{self.tech_queue[0].science} (+{self.get_science()}) [{self.get_research_progress()} turns]')
        else:
            print(f'\tscience: +{self.get_science()}')

        print(f'\tresearch: {self.researched}')

        print(f'\tgold: {self.gold_acc} (+{self.get_gold()})')

        print(f'\thappiness: {self.get_happiness()} (+{self.get_positive_happiness()}, -{self.get_negative_happiness()})')

        print(f'\tculture: {self.culture_acc}/{self.get_social_policy_culture_req()} (+{self.get_culture()}) [{self.get_social_policy_progress()} turns]')
        print(f'\tpolicies: {self.social_policies}')

        print(f'\tfaith: {self.faith_acc} (+{self.get_faith()})')
        print()

        print(f'\tresearch queue: {self.tech_queue}')
        print(f'\tsocial policy queue: {self.social_policies_queue}')
        print()

        print(f'\tunits: {self.units}')
        
        # science = 0/25 (+4) []
        # researched = [agriculture]

        # gold = 22 (+3)
        # happiness = 5 (+9, -4)

        # culture = 0/15 (+1) [15 turns]
        # researched = [garrison(tradition)]

        # faith = 0/6 (+0) [inf turns]

        for i, city in self.cities.items():
            print(f'CITY {i}')
            city.stats()
            print()

    def next_turn(self):
        # order of actions

        # 1) move units / build tiles / settle cities
        # 2) accumulate gold/turn for cities
        # 3) accumulate gold/turn for whole civ

        # 1)
        for unit in self.units.values():
            unit.next_turn()
        
        self.cleanup_units()

        # 2)
        for city in self.cities.values():
            city.next_turn()

        # 3)
        self.gold_acc += self.get_gold()
        self.faith_acc += self.get_faith()
        self.culture_acc += self.get_culture()
        self.science_acc += self.get_science()
        self.happiness_acc += self.get_happiness()

        if self.tech_queue and self.science_acc >= self.tech_queue[0].science:
            self.science_acc -= self.tech_queue[0].science
            self.researched.append(self.tech_queue.pop(0))

        culture_req = self.get_social_policy_culture_req()
        if self.social_policies_queue and self.culture_acc >= culture_req:
            self.culture_acc -= culture_req
            self.social_policies.append(self.social_policies_queue.pop(0))
    

    def add_unit_made_listener(self, listener: IUnitMadeListener):
        self.unit_made_listeners.append(listener)

    def add_city_made_listener(self, listener: ICityMadeListener):
        self.city_made_listeners.append(listener)

