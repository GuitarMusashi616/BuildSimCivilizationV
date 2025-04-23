
from typing import List
from researchable.Policy import Policy


class PolicyFactory:
    @staticmethod
    def from_string_list(policies: List[str]) -> List[Policy]:
        return [Policy(x) for x in policies]

    @staticmethod
    def oligarchy():
        return Policy('Oligarchy')