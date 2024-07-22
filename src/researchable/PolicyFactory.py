
from researchable.Policy import Policy


class PolicyFactory:
    @staticmethod
    def oligarchy():
        return Policy('Oligarchy')