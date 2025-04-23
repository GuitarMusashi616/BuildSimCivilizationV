# pyright: strict

from core.ICity import ICity
from core.ICiv import ICiv


class Granary:
    def __init__(self):
        pass

    def on_create(self, city: ICity, civ: ICiv):
        "Improve tile yields"

    def on_destroy(self, city: ICity, civ: ICiv):
        "Reverse tile yield improvements"