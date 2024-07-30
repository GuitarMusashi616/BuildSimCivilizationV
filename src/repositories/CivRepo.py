from core.Civ import Civ


class CivRepo:
    def __init__(self):
        self.civs = {}

    def put(self, id: int, civ: Civ):
        self.civs[id] = civ
        
    def get(self, id: int) -> Civ:
        assert id in self.civs, f"Civ with id {id} does not exist"
        return self.civs[id]
