# pyright: basic

import math
from typing import List
from core.City import City
from util.Formula import Formula
from enums.Nation import Nation
from researchable.Policy import Policy
from researchable.Tech import Tech

STARTING_HAPPINESS = 9

class Civ:
    def __init__(self, nation: Nation):
        self.nation = nation

        self.research_queue: List[Tech] = []
        self.researched: List[Tech] = []
        self.social_policies_queue: List[Policy] = []
        self.social_policies: List[Policy] = []
        self.cities: List[City] = []

        self.gold_acc = 0
        self.science_acc = 0
        self.culture_acc = 0
        self.faith_acc = 0
        self.happiness_acc = 0

    def queue_research(self, research: Tech):
        self.research_queue.append(research)

    def queue_social_policy(self, policy: Policy):
        self.social_policies_queue.append(policy)
    
    def add_city(self, city: City):
        self.cities.append(city)

    def get_gold(self):
        return sum(x.get_gold() for x in self.cities)

    def get_positive_happiness(self):
        return STARTING_HAPPINESS

    def get_total_pop(self):
        return sum(x.get_pop() for x in self.cities)

    def get_negative_happiness(self):
        return len(self.cities)*3 + self.get_total_pop()

    def get_happiness(self):
        return self.get_positive_happiness() - self.get_negative_happiness()

    def get_science(self):
        return sum(x.get_science() for x in self.cities)

    def get_culture(self):
        return sum(x.get_culture() for x in self.cities)

    def get_faith(self):
        return sum(x.get_faith() for x in self.cities)

    def get_research_progress(self):
        try:
            return math.ceil((self.research_queue[0].science - self.science_acc) / self.get_science())
        except ZeroDivisionError:
            return -1

    def get_social_policy_culture_req(self):
        return Formula.culture_required_for_social_policy(len(self.social_policies), len(self.cities))

    def get_social_policy_progress(self):
        try:
            return math.ceil((self.get_social_policy_culture_req() - self.culture_acc) / self.get_culture())
        except ZeroDivisionError:
            return -1

    def stats(self):
        print("CIVILIZATON STATS")
        if len(self.research_queue) > 0:
            print(f'\tscience: {self.science_acc}/{self.research_queue[0].science} (+{self.get_science()}) [{self.get_research_progress()} turns]')
        else:
            print(f'\tscience: +{self.get_science()}')

        print(f'\tresearch: {self.researched}')

        print(f'\tgold: {self.gold_acc} (+{self.get_gold()})')

        print(f'\thappiness: {self.get_happiness()} (+{self.get_positive_happiness()}, -{self.get_negative_happiness()})')

        print(f'\tculture: {self.culture_acc}/{self.get_social_policy_culture_req()} (+{self.get_culture()}) [{self.get_social_policy_progress()} turns]')
        print(f'\tpolicies: {self.social_policies}')

        print(f'\tfaith: {self.faith_acc} (+{self.get_faith()})')
        print()

        print(f'\tresearch queue: {self.research_queue}')
        print(f'\tsocial policy queue: {self.social_policies_queue}')
        print()
        
        # science = 0/25 (+4) []
        # researched = [agriculture]

        # gold = 22 (+3)
        # happiness = 5 (+9, -4)

        # culture = 0/15 (+1) [15 turns]
        # researched = [garrison(tradition)]

        # faith = 0/6 (+0) [inf turns]

        for i, city in enumerate(self.cities):
            print(f'CITY {i+1}')
            city.stats()
            print()

    def next_turn(self):
        self.gold_acc += self.get_gold()
        self.faith_acc += self.get_faith()
        self.culture_acc += self.get_culture()
        self.science_acc += self.get_science()
        self.happiness_acc += self.get_happiness()

        if self.research_queue and self.science_acc >= self.research_queue[0].science:
            self.science_acc -= self.research_queue[0].science
            self.researched.append(self.research_queue.pop(0))

        culture_req = self.get_social_policy_culture_req()
        if self.social_policies_queue and self.culture_acc >= culture_req:
            self.culture_acc -= culture_req
            self.social_policies.append(self.social_policies_queue.pop(0))

        for city in self.cities:
            city.next_turn()