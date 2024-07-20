# pyright: basic

from Wonder import Wonder


class City:
    def __init__(self):
        self.pop = 1
        self.tiles = []
        self.wonders = []
        self.buildings = []
    
    def add_wonder(self, wonder: Wonder):
        self.wonders.append(wonder)
    

