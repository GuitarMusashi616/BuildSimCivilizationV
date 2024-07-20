# pyright: strict

from typing import List
from Resource import Resource
from Improvement import Improvement

from dataclasses import dataclass

@dataclass
class Tile:
    """Keeps track of tile and improvements on that tile that make up a city"""

    food: int
    prod: int
    gold: int
    resources: List[Resource]
    improvements: List[Improvement]

    # def __init__(self, food: int, prod: int, gold: int, resources: List[Resource]):
    #     pass