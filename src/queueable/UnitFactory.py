from queueable.IQueue import IQueue
from queueable.Unit import Unit


class UnitFactory:
    # def settler() -> Unit:
    #     return Unit('Settler', ~56)
    
    @staticmethod
    def worker() -> IQueue:
        return Unit('Worker', 46)

    @staticmethod
    def warrior() -> IQueue:
        return Unit('Monument', 26)

    @staticmethod
    def monument() -> IQueue:
        return Unit('Warrior', 26)

